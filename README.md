# RAG Tutorials

This repository contains a collection of Jupyter notebooks demonstrating various aspects of Retrieval Augmented Generation (RAG).

## Notebooks

### 1. [`multi-agent-system.ipynb`](./multi-agent-system.ipynb)

This notebook showcases the implementation of a multi-agent system. It defines and orchestrates multiple agents, including a web researcher, a RAG agent, and an NL2SQL agent, to handle complex queries. The system uses a supervisor to route tasks to the appropriate agent based on the user's request. Key components include:

- Setting up API keys for Tavily and Google Gemini.
- Defining agent states and tools (web search, RAG, NL2SQL).
- Creating individual agents and a supervisor node.
- Visualizing the control flow of the multi-agent system.
- Testing the system with various queries.

### 2. [`rag_from_scatch.ipynb`](./rag_from_scatch.ipynb)

This notebook demonstrates how to build a RAG system from scratch. It covers the fundamental steps involved in creating a RAG pipeline without relying heavily on pre-built libraries for the core RAG logic. The process includes:

- Preparing a dataset (cat facts).
- Loading embedding and language models using Ollama.
- Creating a vector database by generating embeddings for text chunks.
- Defining a cosine similarity function to compare embeddings.
- Implementing a retriever to find relevant chunks for a given query.
- Performing RAG by combining retrieved knowledge with a language model to generate answers.

### 3. [`rag_with_langchain.ipynb`](./rag_with_langchain.ipynb)

This notebook illustrates how to build a RAG system using the LangChain library. It simplifies the development process by leveraging LangChain's components for document loading, text splitting, embedding, vector storage, and creating RAG chains. The notebook covers:

- Defining chat and embedding models (e.g., Google Gemini).
- Setting up an in-memory vector store.
- Ingesting data from a web source (Lilian Weng's blog post on agents).
- Splitting documents into manageable chunks.
- Defining a RAG chain/graph using LangChain Expression Language (LCEL).
- Visualizing the control flow of the RAG application.
- Performing RAG to answer questions based on the ingested documents.

## Setup

Please refer to the individual notebooks for specific setup instructions and dependencies. Generally, you will need to:

1.  Install Python and Jupyter Notebook/JupyterLab.
2.  Install required Python packages listed in `requirements.txt` (if available) or within the notebooks themselves.
3.  Set up API keys for services like Google Gemini, Tavily, etc., as indicated in the notebooks.
4.  For `rag_from_scatch.ipynb`, ensure Ollama is installed and the specified models are pulled.
5.  For `multi-agent-system.ipynb`, ensure the `ecommerce.db` is set up by running `db_setup.py` and necessary document files are present in the `content/docs` directory.

## Usage

Open the Jupyter notebooks and run the cells sequentially to understand and execute the RAG implementations.
