# atax_ai_tui

# AI Chat TUI

A terminal-based chat application with a **Textual User Interface (TUI)** that allows you to interact with an AI model via OpenRouter. The app features a **red/green/yellow theme**, smooth borders, and supports chat history, language settings, and more.

## ✨ Features

- **TUI Interface**: Built with [Textual](https://textual.textualize.io/), a modern TUI framework for Python.
- **AI Chat**: Communicate with an AI model via OpenRouter.
- **Chat History**: All conversations are saved locally in `chats.json`.
- **Smooth Theme**: Red/green/yellow theme with rounded borders.
- **Time Display**: Shows current time in the top-right corner.
- **Status Bar**: Provides shortcuts and instructions at the bottom.
- **Responsive Layout**: Toggle sidebar, multi-line input, and more.
- **Keyboard Shortcuts**: Easy navigation using keys like `q`, `n`, `h`, and `Tab`.

## 📦 Installation

### Prerequisites

- Python 3.8 or higher.
- An OpenRouter API key (get one [here](https://openrouter.ai/)).

### 1. Clone the Repository

```bash
git clone https://github.com/linuxtopG/atax_ai_tui.git
cd atax_ai_tui.git
```
####  vnve setup
```
python3 -m venv tuiai
```
```
source tuiai/bin/activate
```
### Install Required Libraries >>Create a config.json file in the project directory:
```
pip install textual openai
```
###  Configure Your API Key
```
{
  "api_key": "YOUR_OPENROUTER_API_KEY",
  "model": "openchat/openchat-7b:free"
}
```

ذذ
