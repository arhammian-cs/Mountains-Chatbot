https://mountains-chatbot-2.streamlit.app/


# 🇵🇰 Pakistan Travel Assistant

A Streamlit-based AI chatbot that helps users plan domestic trips within Pakistan — destinations, itineraries, budgets, transportation, and more. Built with LangChain and OpenAI's GPT-4o-mini.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-app-red.svg)

## ✨ Features

- Conversational AI focused exclusively on **domestic tourism in Pakistan**
- Covers Hunza, Skardu, Gilgit, Naran, Kaghan, Swat, Murree, Chitral, Neelum Valley, Fairy Meadows, and more
- Trip planning, day-by-day itineraries, budget estimates, and travel tips
- Clean, premium UI with a mountain-themed background
- Session-based chat history (new chat / previous sessions in sidebar)
- Domain-restricted: politely declines unrelated questions (international travel, coding, etc.)

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in your terminal (usually `http://localhost:8501`), and enter your OpenAI API key on the start screen.

## 🔐 API Key

Your OpenAI API key is entered directly in the app and is kept only in the current browser session (`st.session_state`) — it is never written to disk or committed to this repo. Never hardcode your API key in `app.py` or commit it to GitHub.

## 🗂️ Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — web app framework
- [LangChain](https://www.langchain.com/) — LLM orchestration
- [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models) — language model

## 📄 License

This project is open source. Add your preferred license (e.g. MIT) here.
