# INSIGHTDOCS.AI

AI-powered document intelligence system built using Retrieval Augmented Generation (RAG) to enable semantic document search and context-aware question answering over PDF documents.

## Features

* Upload PDF documents
* Semantic document retrieval using vector search
* Context-aware question answering
* Local document understanding using embeddings
* FastAPI backend architecture
* Streamlit interactive frontend
* Groq LLM API integration for fast inference

## Architecture

PDF Upload
→ PDF Parsing
→ Text Chunking
→ Embedding Generation
→ ChromaDB Vector Storage
→ Semantic Retrieval
→ Groq LLM Inference
→ AI Response Generation

## Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq API
* Docker

## Example Queries

* Summarize this document
* What technologies are discussed in this paper?
* Explain the architecture proposed in this paper
* What problem does this research solve?

## Run Project

Backend

python -m uvicorn api:app --reload

Frontend

streamlit run app.py
