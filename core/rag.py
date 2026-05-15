# core/rag.py
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma_db"

def get_retriever(k: int = 3):
    """
    Load the ChromaDB vector store and return a retriever.

    Args:
        k: Number of most relevant chunks to retrieve per query.
           3 is a good default — enough context, not too noisy.

    Returns:
        A LangChain retriever object ready to use.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
    return retriever

def get_context(query: str, k: int = 3) -> str:
    """
    Given a code query, find the most relevant chunks from the codebase.

    Args:
        query: The code or question to search for.
        k: Number of chunks to return.

    Returns:
        A single string combining all relevant chunks.
    """
    retriever = get_retriever(k=k)
    docs = retriever.invoke(query)

    if not docs:
        return ""

    # Join all retrieved chunks into one context string
    context_parts = []
    for i, doc in enumerate(docs):
        source = doc.metadata.get("source", "unknown")
        context_parts.append(f"--- Chunk {i+1} from {source} ---\n{doc.page_content}")

    return "\n\n".join(context_parts)