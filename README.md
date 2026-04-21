# 🚀 LangChain Models & Embeddings Playground

> A hands-on exploration of LLMs, Chat Models, and Embeddings using LangChain.

---

## 📌 Overview

This repository contains my practical experiments with **LangChain**, focusing on understanding how modern AI systems work in real-world applications.

It covers:
- LLMs vs Chat Models
- Multiple API providers (Groq, OpenAI, Gemini, HuggingFace)
- Open-source vs Closed-source models
- Embeddings (HuggingFace, Cohere)
- Semantic Search & Document Retrieval

---

## 📂 Project Structure

## 📂 Project Structure

```text
LANGCHAIN_MODELS/
├── ChatModels/
│   ├── 1_chatmodel_groq.py
│   ├── 2_chatmodel_openai.py
│   ├── 3_chatmodel_google.py
│   ├── 4_chatmodel_hf_api.py
│   └── 5_chatmodel_hf_local.py
├── EmbeddedModels/
│   ├── embed_cohere.py
│   ├── embed_hugging_sentence.py
│   ├── embedding_cohere_docs.py
│   └── similarity_doc_retr.py
├── LLMs/
│   └── llm_demo.py
├── .env
├── .gitignore
├── requirements.txt
└── test.py

---

## 🔥 What I Learned

- Difference between **LLMs and Chat Models**
- Working with multiple providers:
  - Groq
  - OpenAI
  - Google Gemini
  - HuggingFace (API & Local)
- Using **Embeddings for vector representation**
- Performing **Semantic Search**
- Basics of **Retrieval-Augmented Generation (RAG)**

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/codehacker4655/Langchain_llm_model_experiments.git  
cd Langchain_llm_model_experiments  

---

### 2. Create virtual environment

python -m venv venv  

Activate:

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

---

### 3. Install dependencies

pip install -r requirements.txt  

---

### 4. Add API Keys

Create a `.env` file in root directory:

GROQ_API_KEY=your_key  
OPENAI_API_KEY=your_key  
GOOGLE_API_KEY=your_key  
HUGGINGFACEHUB_API_TOKEN=your_key  
COHERE_API_KEY=your_key  

---

## 🧪 Example Usage

Run any script:

python ChatModels/1_chatmodel_groq.py  

or

python EmbeddedModels/similarity_doc_retr.py  

---

## 🚀 Future Improvements

- Build a complete **RAG pipeline**
- Add **Streamlit UI**
- Integrate **Vector Databases (FAISS, Chroma)**
- Add evaluation metrics

---

## 🤝 Contributing

This is a personal learning project, but suggestions are welcome!

---

## ⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!
