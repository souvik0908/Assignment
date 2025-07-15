# 🧠 Reddit Persona Generator

This Python CLI tool scrapes Reddit activity from a user profile and generates a structured persona using an AI model through [OpenRouter](https://openrouter.ai).  
Built for internship evaluation — follows best practices and is CLI-first.

---

## 📌 Features

- Fetches up to 100 recent comments and 50 submissions
- Sends content to AI via OpenRouter (DeepSeek / Claude / GPT)
- Outputs a detailed persona (markdown format) with post references
- Uses `.env` for secure API key management
- No frontend needed — terminal only

---

## 🚀 Installation and Setup

---

### 🐍 2. Create a Virtual Environment

#### On Linux/macOS:

```bash
python3 -m venv venv

source venv/bin/activate
