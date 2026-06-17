from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import ollama


def ask_question(query):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    # SUMMARY MODE
    summary_queries = [
        "summary",
        "summarize",
        "tell me summary",
        "what is this document about",
        "give me summary"
    ]

    # if generic summary → fetch many chunks
    if query.lower() in summary_queries:
        docs = db.similarity_search("", k=50)

    # normal question → semantic retrieval
    else:
        docs = db.similarity_search(query, k=8)

    print("Retrieved docs:", len(docs))

    if len(docs) == 0:
        return "No document found"

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are a document assistant.

RULES:
1. If user asks for summary, summarize the COMPLETE document.
2. If user asks specific question, answer from document only.
3. Do not invent information.
4. Give clear answers.

DOCUMENT:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]