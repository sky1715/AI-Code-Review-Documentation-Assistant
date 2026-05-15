# ingest/indexer.py
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma_db"       # folder where vectors will be stored
CODE_PATH   = "sample_code"     # folder of .py files to index

def get_embeddings():
    """
    Load the HuggingFace embedding model.
    Downloads once, then cached locally.
    'all-MiniLM-L6-v2' is small (80MB), fast, and great for code.
    """
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

def load_documents():
    """
    Load all .py files from sample_code/ folder.
    Each file becomes a LangChain Document object.
    """
    loader = DirectoryLoader(
        CODE_PATH,
        glob="**/*.py",          # find all .py files recursively
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} files from {CODE_PATH}/")
    return docs

def split_documents(docs):
    """
    Split documents into smaller chunks.
    Why? LLMs have token limits — we can't send entire files.
    chunk_size=500: each chunk is ~500 characters
    chunk_overlap=50: chunks share 50 chars so context isn't lost at edges
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks")
    return chunks

def build_vectorstore(chunks):
    """
    Embed all chunks and store in ChromaDB.
    This creates a chroma_db/ folder in your project.
    """
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"Stored {len(chunks)} chunks in ChromaDB at '{CHROMA_PATH}/'")
    return vectorstore

def index_codebase():
    """Main function — run this once to index your code."""
    print("Starting indexing...")
    docs   = load_documents()
    chunks = split_documents(docs)
    store  = build_vectorstore(chunks)
    print("Indexing complete!")
    return store

if __name__ == "__main__":
    index_codebase()