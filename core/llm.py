# core/llm.py
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Send a system + user message to Groq and return the response.

    Args:
        system_prompt: Instructions that control the LLM's behaviour.
        user_prompt: The actual content to process (e.g. code to review).

    Returns:
        The LLM's response as a string.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},  # persona + rules
            {"role": "user",   "content": user_prompt}     # the actual task
        ],
        temperature=0.1,   # very low = consistent structured output
        max_tokens=1000
    )
    return response.choices[0].message.content