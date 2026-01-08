import json
import time
from datetime import datetime
from openai import OpenAI
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, RichLog, Input, Button, Static, ListView, ListItem
from textual.reactive import reactive
from textual import events
from textual.timer import Timer

# CSS محدث - ثيم أحمر/أخضر/أصفر مع حواف ناعمة
CSS = """
Screen {
    background: black;
}

#sidebar {
    width: 30;
    background: #0a0a0a;
    border: round #ff0000;
    border-title-color: #ff0000;
    padding: 1;
    margin: 0;
}

#main_container {
    background: #0a0a0a;
    border: round #00ff00;
    padding: 1;
    margin: 0;
}

#input_container {
    height: auto;
    min-height: 3;
    border: round #ffff00;
    padding: 0 1;
    margin: 0;
}

#chat_log {
    height: 1fr;
    border: round #ff00ff;
    background: #000;
    padding: 0 1;
    margin: 0;
}

#chats_list {
    background: #000;
    color: #0f0;
    border: round #f0f;
    padding: 0 1;
    margin: 0;
}

Input {
    background: #111;
    color: #ffff00;
    border: round #ff0000;
    padding: 0 1;
    height: auto;
    min-height: 1;
    max-height: 5;
    margin: 0;
}

Input:focus {
    border: double #ffff00;
}

Button {
    border: round #00ff00;
    background: #000;
    color: #ffff00;
    width: 100%;
    margin: 1 0;
}

Button:hover {
    background: #111100;
    color: #ff0000;
}

.hidden {
    width: 0;
    border: none;
    padding: 0;
    display: none;
}

#time_display {
    align: right middle;
    color: #ffff00;
    background: #000;
    border: none;
    padding: 0 1;
}

#status_bar {
    background: #000;
    color: #ffffff;
    border: round #555555;
    padding: 0 1;
    height: 1;
}
"""

class NeonButton(Button):
    pass

class ChatItem(ListItem):
    def __init__(self, chat_id: str, title: str):
        super().__init__()
        self.chat_id = chat_id
        self.title = title
        self.label = Static(f"{title}")
        self.compose_add_child(self.label)

class AIChatApp(App):
    CSS = CSS
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("n", "new_chat", "New Chat"),
        ("h", "toggle_sidebar", "Hide/Show Sidebar"),
    ]

    sidebar_visible = reactive(True)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="sidebar", classes="hidden" if not self.sidebar_visible else "") as sidebar:
                sidebar.border_title = "Chats"
                yield NeonButton("1. New Chat (n)", id="new_chat_btn")
                yield NeonButton("2. Hide (h)", id="toggle_sidebar_btn")
                yield ListView(id="chats_list")
            with Container(id="main_container"):
                yield Static(id="time_display")  # عرض الوقت
                yield RichLog(id="chat_log", wrap=True, markup=True)
                with Container(id="input_container"):
                    yield Input(placeholder="Type your message here...", id="input_box")
        yield Static(id="status_bar")

    def on_mount(self):
        self.chat_log = self.query_one("#chat_log")
        self.input_box = self.query_one("#input_box")
        self.chats_list = self.query_one("#chats_list")
        self.time_display = self.query_one("#time_display")
        self.status_bar = self.query_one("#status_bar")

        # بدء مؤقت لتحديث الوقت
        self.set_interval(1, self.update_time)

        # تحميل معلومات التكوين
        with open("config.json", "r") as f:
            config = json.load(f)
        self.api_key = config["api_key"]
        self.model = config["model"]
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://openrouter.ai/api/v1",
        )

        self.current_chat_id = "chat_" + str(int(time.time()))
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        self.chats = self.load_chats()
        self.refresh_chats_list()

        # عرض الترخيص
        self.chat_log.write("[bold blue]🤖 AI: Hello! How can I help you?[/bold blue]")

        # تحديث شريط الحالة مع ملاحظات مفصلة
        self.status_bar.update(
            "[bold red]q[/bold red] Quit | "
            "[bold green]n[/bold green] New Chat | "
            "[bold yellow]h[/bold yellow] Hide/Show Sidebar | "
            "[bold cyan]Tab[/bold cyan] Toggle Sidebar"
        )

    def update_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.time_display.update(f"[bold yellow]{now}[/bold yellow]")

    def load_chats(self):
        try:
            with open("chats.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_chats(self):
        with open("chats.json", "w", encoding="utf-8") as f:
            json.dump(self.chats, f, ensure_ascii=False, indent=2)

    def refresh_chats_list(self):
        self.chats_list.clear()
        for chat_id, data in self.chats.items():
            item = ChatItem(chat_id, data.get("title", "Untitled Chat"))
            self.chats_list.append(item)

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "new_chat_btn":
            self.action_new_chat()
        elif event.button.id == "toggle_sidebar_btn":
            self.action_toggle_sidebar()

    def on_input_submitted(self, message):
        user_input = message.value
        if not user_input.strip():
            return

        # تحديث المحادثة الحالية
        self.messages.append({"role": "user", "content": user_input})
        self.chat_log.write(f"[bold green]👤 You:[/bold green] {user_input}")
        self.input_box.value = ""

        # حفظ المحادثة الحالية
        self.chats[self.current_chat_id] = {
            "title": self.messages[1]["content"][:30] if len(self.messages) > 1 else "New Chat",
            "messages": self.messages,
            "timestamp": datetime.now().isoformat()
        }
        self.save_chats()
        self.refresh_chats_list()

        # استدعاء الذكاء الاصطناعي
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
            )
            ai_response = completion.choices[0].message.content
            self.messages.append({"role": "assistant", "content": ai_response})
            self.chat_log.write(f"[bold blue]🤖 AI:[/bold blue] {ai_response}")

            # تحديث المحادثة بعد الرد
            self.chats[self.current_chat_id]["messages"] = self.messages
            self.save_chats()
        except Exception as e:
            self.chat_log.write(f"[bold red]Error:[/bold red] {str(e)}")

    def on_list_view_selected(self, event: ListView.Selected):
        chat_id = event.item.chat_id
        data = self.chats[chat_id]
        self.current_chat_id = chat_id
        self.messages = data["messages"]
        self.chat_log.clear()
        for msg in self.messages[1:]:  # تخطي الرسالة النظامية
            role = "🤖 AI" if msg["role"] == "assistant" else "👤 You"
            color = "blue" if msg["role"] == "assistant" else "green"
            self.chat_log.write(f"[bold {color}]{role}:[/bold {color}] {msg['content']}")

    def action_new_chat(self):
        self.current_chat_id = "chat_" + str(int(time.time()))
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        self.chat_log.clear()
        self.chat_log.write("[bold blue]🤖 AI: Hello! How can I help you?[/bold blue]")

    def action_toggle_sidebar(self):
        self.sidebar_visible = not self.sidebar_visible
        sidebar = self.query_one("#sidebar")
        if self.sidebar_visible:
            sidebar.remove_class("hidden")
        else:
            sidebar.add_class("hidden")

    def on_key(self, event: events.Key):
        if event.key == "tab":
            self.action_toggle_sidebar()

if __name__ == "__main__":
    AIChatApp().run()
