import praw
import os
import re
import argparse
import json
from datetime import datetime
from dotenv import load_dotenv
import requests  # ✅ REQUIRED for OpenRouter

load_dotenv()

# Configuration
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = 'PersonaGenerator/1.0 by YourName'
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_MODEL = "tngtech/deepseek-r1t2-chimera:free"  # Or choose another OpenRouter model

def extract_username(url):
    pattern = r'https?://www\.reddit\.com/user/([^/]+)/?'
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid Reddit profile URL")
    return match.group(1)

def get_reddit_content(username):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    
    user = reddit.redditor(username)
    content = []

    for comment in user.comments.new(limit=100):
        content.append({
            "id": f"t1_{comment.id}",
            "type": "comment",
            "text": comment.body,
            "subreddit": comment.subreddit.display_name,
            "created_utc": comment.created_utc
        })

    for submission in user.submissions.new(limit=50):
        content.append({
            "id": f"t3_{submission.id}",
            "type": "submission",
            "title": submission.title,
            "text": submission.selftext,
            "subreddit": submission.subreddit.display_name,
            "created_utc": submission.created_utc
        })
    
    return content

def generate_persona(username, content):
    if not content:
        return "No content available for persona generation."

    system_prompt = (
        "You're an expert UX researcher. Create a detailed user persona from Reddit activity. "
        "Include these sections:\n"
        "1. Background (location if available)\n"
        "2. Interests (hobbies)\n"
        "3. Behavioral Traits (engagement style, tone)\n"
        "4. Values/Preferences\n"
        "5. Potential Goals\n"
        "6. Pain Points\n\n"
        "For EACH characteristic:\n"
        "- Cite specific content IDs in brackets like [t3_abc123]\n"
        "- Include ONLY characteristics supported by evidence\n"
        "Use markdown formatting with clear section headers."
    )

    user_content = json.dumps(content, ensure_ascii=False)[:12000]

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Username: {username}\nContent:\n{user_content}"}
        ],
        "temperature": 0.3,
        "max_tokens": 1500
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"OpenRouter API Error: {response.status_code} - {response.text}")

def save_persona(username, persona):
    filename = f"{username}_persona.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Reddit User Persona Report\n")
        f.write(f"Profile: https://www.reddit.com/user/{username}/\n\n")
        f.write(persona)
    return filename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Reddit profile URL')
    args = parser.parse_args()

    try:
        username = extract_username(args.url)
        print(f"Fetching data for: {username}")
        content = get_reddit_content(username)
        print(f"Found {len(content)} content items")
        persona = generate_persona(username, content)
        filename = save_persona(username, persona)
        print(f"Persona saved to: {filename}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
