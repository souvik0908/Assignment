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
```
On Windows (CMD):
```cmd
Copy
Edit
python -m venv venv
venv\Scripts\activate
```
📦 4. Install Required Dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
🔐 5. Set Up Environment Variables
Create a .env file in the root directory and add the following:

env
Copy
Edit
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
OPENROUTER_API_KEY=your_openrouter_api_key
💡 Get Reddit API credentials: https://www.reddit.com/prefs/apps
💡 Get OpenRouter API key: https://openrouter.ai/
