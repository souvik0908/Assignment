# 🧠 Reddit Persona Generator

This Python script fetches a public Reddit user's recent activity and generates a detailed UX-style persona using an AI language model via [OpenRouter](https://openrouter.ai). It's built for intern assignment submission purposes and adheres to PEP-8 standards.

---

## 📌 Features

- 🔍 Fetches up to 100 recent comments + 50 posts for any Reddit user
- 🤖 Sends content to an AI model (e.g., DeepSeek/Claude/GPT) via OpenRouter
- 📝 Outputs a Markdown-formatted persona with behavioral, interest-based, and psychological traits
- 🔒 Keeps secrets like API keys safely in a `.env` file
- ✅ Fully CLI-automated; no GUI required

---

## 🚀 Quick Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/souvik0908/Assignment.git
cd Assignment
---
### 2. Set up a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
# On Windows (CMD):
# venv\Scripts\activate
###3. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
### 🔐 Environment Variables
Create a .env file in the root of your project with the following:

ini
Copy
Edit
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
OPENROUTER_API_KEY=your_openrouter_api_key
💡 You can get Reddit credentials by registering an app at: https://www.reddit.com/prefs/apps
💡 You can get an OpenRouter key here: https://openrouter.ai/

### 🧪 Run the Script
bash
Copy
Edit
python reddit_persona.py https://www.reddit.com/user/<username>/
Example:

bash
Copy
Edit
python reddit_persona.py https://www.reddit.com/user/kojied/
### ✅ The output will be saved as:

Copy
Edit
kojied_persona.txt
