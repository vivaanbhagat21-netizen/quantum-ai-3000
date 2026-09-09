# Quantum AI (Python Desktop & CLI App)

⚡ **Quantum AI** is a live web-connected assistant that runs standalone **away from the web browser** as a native Desktop GUI app or interactive command-line app.

---

## 🚀 Quick Start (No Browser Required!)

### 1. Run Desktop GUI (Default)

Double click `run.bat` or execute in terminal:

```bash
python app.py
```

### 2. Run Interactive CLI Mode

```bash
python app.py --cli
```

---

## ✨ Features

- 🎨 **Web-matching Aesthetics**: Dark obsidian theme `#0a0a0f`, neon cyan/purple accents, glowing status indicators, and formatted message bubbles matching the original web app.
- 🔎 **Live Web Search**: DuckDuckGo Instant Answers + DuckDuckGo HTML web search + Wikipedia REST API.
- ⛅ **Real-Time Weather**: Query live weather anywhere (e.g. `weather in Tokyo`).
- 🌐 **Web Page Reader**: Paste any URL directly into chat to fetch page text & snippets.
- 🧠 **Conversation Memory**: Remembers context across follow-up questions; handles `clear memory` and `what do you remember?`.
- ⚙️ **Optional LLM Synthesis**: Add your OpenAI API key in the settings panel or `.env` for AI-synthesized responses.
- 💾 **Export Chat History**: Save chat logs directly to file.

---

## ⚙️ Requirements

- Python 3.8+ (Standard Library `urllib`, `tkinter`, `json`, `re` built-in out of the box).
- Optional: `pip install -r requirements.txt` for `requests` and `openai` support.

---

## 📁 File Structure

```
quantum-ai/
├── app.py                 # Main entry point (GUI default, --cli flag)
├── run.bat                # Windows 1-click Desktop launcher
├── run_cli.bat            # Windows CLI launcher
├── requirements.txt       # Optional dependencies
└── quantum_ai/            # Core Python package
    ├── __init__.py
    ├── memory.py          # Memory, tokenization, context resolution & ranking
    ├── search.py          # Web search, weather & URL fetch engine
    ├── engine.py          # Live response generator
    ├── gui.py             # Tkinter dark obsidian Desktop GUI
    └── cli.py             # Terminal CLI interface
```
