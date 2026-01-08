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
###  Configure Your API Key in "config.json"
```
{
  "api_key": "YOUR_OPENROUTER_API_KEY",
  "model": "openchat/openchat-7b:free"
}
```
### free Models in "https://openrouter.ai/models?q=free"
```
xiaomi/mimo-v2-flash:free
```

```
mistralai/devstral-2512:free
```
```
tngtech/deepseek-r1t2-chimera:free
```
```
kwaipilot/kat-coder-pro:free
```
```
nex-agi/deepseek-v3.1-nex-n1:free
```

```
tngtech/deepseek-r1t-chimera:free
```

```
nvidia/nemotron-3-nano-30b-a3b:free
```
```
qwen/qwen3-coder:free
```
```
nvidia/nemotron-nano-12b-v2-vl:free
```
```
z-ai/glm-4.5-air:free
```
```
tngtech/tng-r1t-chimera:free
```
```
deepseek/deepseek-r1-0528:free
```
```
google/gemma-3-27b-it:free
```
```
meta-llama/llama-3.3-70b-instruct:free
```
```
cognitivecomputations/dolphin-mistral-24b-venice-edition:free
```
```
google/gemini-2.0-flash-exp:free
```
```
openai/gpt-oss-120b:free
```
```
nousresearch/hermes-3-llama-3.1-405b:free
```
```
openai/gpt-oss-20b:free
```
```
mistralai/mistral-7b-instruct:free
```
```
meta-llama/llama-3.1-405b-instruct:free
```
```
mistralai/mistral-small-3.1-24b-instruct:free
```
```
nvidia/nemotron-nano-9b-v2:free
```
```
arcee-ai/trinity-mini:free
```
```
qwen/qwen3-4b:free
```
```
meta-llama/llama-3.2-3b-instruct:free
```
```
qwen/qwen-2.5-vl-7b-instruct:free
```
```
google/gemma-3n-e2b-it:free
```
```
google/gemma-3-4b-it:free
```
```
google/gemma-3-12b-it:free
```
```
google/gemma-3n-e4b-it:free
```
```
moonshotai/kimi-k2:free
```

