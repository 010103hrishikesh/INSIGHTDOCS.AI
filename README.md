# INSIGHTDOCS.AI

An intelligent document assistant built to process PDF documents, retrieve relevant context using semantic search, and generate accurate responses using local language models.

## Project Overview

This project allows users to upload PDF documents and interact with them through natural language queries.

The system extracts document text, converts it into embeddings, stores the embeddings inside a vector database, retrieves relevant content based on similarity search, and uses a local LLM to generate context-aware answers.

## Workflow

* Upload PDF Document
* Extract Text from PDF
* Split Text into Chunks
* Generate Embeddings
* Store in Vector Database
* Retrieve Relevant Chunks
* Generate Response using Local LLM

## Technologies

* Python
* FastAPI
* Streamlit
* LangChain
* ChromaDB
* Ollama
* HuggingFace Embeddings
* Docker

## Functionalities

* PDF Upload and Processing
* Semantic Search
* Context-Aware Question Answering
* Document Summarization
* Local LLM Inference
* Dockerized Backend Deployment

## Run Application

Backend

```bash
python -m uvicorn api:app --reload
```

Frontend

```bash
streamlit run app.py
```

Docker

```bash
docker build -t insightdocs .
docker run -p 8000:8000 insightdocs
```
