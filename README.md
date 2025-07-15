# Reddit User Persona builder using AI

A python based project capable of scraping comments and posts by a redditor and building a user persona using gemini-2.5-flash LLM based on the details found on their reddit. Following are the steps included:

- Scraping content posted on the user profile like comments, posts etc.
- Building a user persona using an LLM.
- Persona saved as a text file.

## Table of contents

-[🚀Features](#🚀features)

-[Setup & Installation](#setup&installation)

-[Usage](#usage)

## 🚀Features

### 🧠 1. AI-Powered Persona Generation
- Uses Google Gemini Pro to generate detailed user personas based on Reddit activity.

- Analyzes tone, interests, values, and personality traits using natural language understanding.

### 🔎 2. Reddit User Scraping
- Accepts a Reddit user profile URL as input.

- Automatically scrapes the user's most recent posts and comments using the Reddit API via praw.

### 📄 3. Structured Output with Citations
Outputs a structured persona including:

- Interests

- Communication style

- Beliefs and values

- Location (if inferred)

- Includes citations to relevant Reddit posts/comments for each insight.

### 🔐 4. Secure API Key Handling
- Uses a .env file to store your Google Gemini API key securely.

- Includes a .gitignore to prevent .env from being tracked in version control.

## 🛠️Setup & Installation
1. **Open your editor**
2. **Open the Terminal** - Typically, you can do this from a 'Terminal' tab or by using a shortcut (e.g., Ctrl + ~ for Windows or Control + ~ for Mac in VS Code).
3. **Clone the Repository and Navigate into the Directory** - Once your terminal is open, you can clone the repository and move into the directory by running the commands below.
