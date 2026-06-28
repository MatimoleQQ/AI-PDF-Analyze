# 📄 AI PDF Assistant

> Full-stack AI web application for interacting with PDF documents using natural language powered by OpenAI GPT-4o-mini.

---

## 🚀 Overview

AI PDF Assistant is a web application that enables users to upload PDF files and ask questions about their content in natural language.
The system extracts and processes document data, then uses an AI model to generate accurate, context-aware answers based on the uploaded file.

---

## ✨ Key Features

* 📤 Upload and process PDF documents
* 💬 Ask questions about document content in natural language
* 🧠 AI-powered answers using OpenAI GPT-4o-mini
* 🔎 Context-based response generation from document data
* ⚡ Fast backend built with FastAPI
* 🌐 Interactive frontend built in React

---

## 🧠 How It Works

1. User uploads a PDF file via the frontend
2. Backend extracts text from the document using Python PDF processing tools
3. Document content is prepared for AI processing
4. User submits a question about the document
5. Relevant context is retrieved from stored data (ChromaDB if used)
6. GPT-4o-mini generates a response based on the context
7. Answer is returned to the frontend in real time

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* OpenAI API (GPT-4o-mini)
* PyPDF

### Frontend

* React
* JavaScript (ES6+)
* HTML / CSS

### Tools & DevOps

* Git
* GitHub

---
### Screenshots

![Main page](screenshots/AI_docs.jpg)
---

## 🧩 Architecture

This project follows a lightweight AI-powered backend architecture:

* REST API handles communication between frontend and backend
* PDF files are processed and converted into text
* AI model generates responses based on extracted content
* Frontend provides chat-like interaction with documents

---

## 💡 Project Highlights

* Built a full-stack AI application from scratch
* Integrated OpenAI API into a real-world use case
* Designed REST API using FastAPI
* Implemented PDF parsing and document processing
* Developed responsive React frontend
* Applied concepts of AI-assisted document understanding

---

## 📌 Potential Improvements

* 🔐 User authentication system
* 📚 Multi-document support
* 💾 Chat history storage
* 📊 Better document indexing (advanced RAG pipeline)
* ⚡ Streaming AI responses
* 📁 File management dashboard

---

## 👨‍💻 Author

Personal project created to explore:

* AI integration in web applications
* Backend development with Python
* Real-world use of LLMs (Large Language Models)
* Retrieval-Augmented Generation concepts
