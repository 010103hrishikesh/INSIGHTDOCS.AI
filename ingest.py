from langchain_community.vectorstores import Chroma
import os
import shutil

from utils.pdf_loader import load_pdf
from utils.chunking import chunk_data
from utils.embeddings import create_embeddings


def ingest(file_path):

    # remove old database
    if os.path.exists("db"):
        shutil.rmtree("db", ignore_errors=True)

    print("Loading PDF...")
    documents = load_pdf(file_path)

    print("Chunking text...")
    chunks = chunk_data(documents)

    print("Creating embeddings...")
    embeddings = create_embeddings()

    print("Creating fresh database...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    db.persist()

    print("Upload complete")