# ⚡ Intelligent NoSQL Database Analyzer
### **AI-powered MongoDB Query Translator, Validator & Optimizer (Offline, Ollama, FastAPI)**

The **Intelligent NoSQL Database Analyzer** is a lightweight, offline AI system designed to translate natural language into MongoDB queries, validate them, and suggest performance improvements including index recommendations.  
Powered by **local LLMs through Ollama**, it runs at zero cost, requires no API keys, and works even without internet.

This project is ideal for:
- Data science & backend engineering portfolios  
- NoSQL + AI demonstration  
- Low-resource machines (no GPU required)  
- Offline AI workflow automation  

---

## 🚀 Features

- 🧠 **Natural Language → MongoDB Query Translator**  
- ✔️ **Query Validator** (syntax check + reasoning)  
- ⚡ **Performance Optimizer** (index recommendations & execution tips)  
- 🤖 **Local LLM Inference via Ollama**  
- 🔌 **Zero dependency on cloud APIs**  
- 🌐 **FastAPI backend** with `/analyze` endpoint  
- 🧩 **Modular Multi-Agent Architecture**  
- 💻 **Lightweight** → works smoothly on low CPU/RAM  

---

## 🏗️ Architecture Diagram

                 ┌──────────────────┐
                 │  FastAPI Server  │
                 │   /analyze API   │
                 └─────────▲────────┘
                           │
                           │ instruction
                           │
  ┌────────────────────────────────────────────────┐
  │                     AGENTS                      │
  │                                                │
  │   ┌────────────────────┐   ┌────────────────┐  │
  │   │ Translator Agent   │   │ Validator Agent│  │
  │   │ NL → Mongo Query   │   │ Syntax Check   │  │
  │   └───────────▲────────┘   └──────▲─────────┘  │
  │               │ query             │ validation │
  │   ┌───────────┴────────┐   ┌─────┴──────────┐ │
  │   │ Optimizer Agent     │   │ LLM Client     │ │
  │   │ Index Suggestions   │   │ (Ollama Local) │ │
  │   └───────────▲────────┘   └────────────────┘ │
  └────────────────────────────────────────────────┘

### Author
Ayush Mishra