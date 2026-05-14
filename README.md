# 🤖 AI Terminal Assistant (LLM CLI)

![Terminal Demonstration](./terminal-screenshot.png)

> *A lightweight Command Line Interface (CLI) tool to interact with Large Language Models directly from the terminal.*

---

## 📖 Overview

As a Senior Backend Developer expanding my stack into the Python ecosystem, I built this CLI application to streamline my development workflow. It allows rapid, context-free querying of Large Language Models (LLMs) without leaving the terminal or switching to a web browser.

The tool handles API communication, parses responses, supports custom model parameters, and gracefully catches API constraints like quota limits.

---

## ✨ Features

- **Direct Terminal Interaction:** Ask questions and get formatted responses straight in your CLI.
- **Parameter Control:** Dynamically adjust the model type and temperature (creativity) via command-line arguments.
- **Robust Error Handling:** Beautifully formatted error handling for API rate limits (`429 insufficient_quota`) and connection issues.
- **Extensible Architecture:** Easily swap API providers (e.g., OpenAI, Google Gemini, Groq, or local Ollama models).

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Hari2892/ai-llm-learning.git
cd ai-llm-learning
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
```

#### Activate the Environment

**Linux / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
API_KEY=your_api_key_here
```

---

## 💻 Usage Examples

### Basic Query

Ask a standard question using the default model settings.

```bash
python llm_cli.py "Explain recursion in simple terms"
```

### Advanced Query with Parameters

Pass specific flags to change the model and adjust the response temperature.

```bash
python llm_cli.py "Write a haiku about coding" --model gpt-4o-mini --temperature 0.3
```

---

## ⚠️ Graceful Error Handling Demonstration

If the API key runs out of credits, the CLI catches the `429` status code and returns a clean, user-friendly error rather than crashing.

### Example Error Output

```text
❌ Error:
Status: 429
Code: insufficient_quota
Message: You exceeded your current quota, please check your plan and billing details.
```

This improves developer experience by providing clear diagnostics and preventing unexpected application termination.

---

## 🛠️ Tech Stack

### Language
- Python 3.x

### Libraries
- `requests` — HTTP client for API communication
- `argparse` — CLI argument parsing
- `python-dotenv` — Environment variable management

### APIs
- OpenAI REST API
- Expandable to Gemini / Groq / Ollama integrations

---

## 🛠 Example Output

```text
Recursion is when a function calls itself
to solve a smaller version of the same problem
until it reaches a stopping point.
```

---

## 👨‍💻 Author

### Hariharan R
Senior PHP & Full-Stack Developer

- Portfolio: [https://hariharan-bio-site.netlify.app/]
- LinkedIn: [https://linkedin.com/in/hariharan-r-55158515a]