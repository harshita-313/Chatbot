# chatbot
# 🧠 Local General Knowledge Chatbot (Mistral + Ollama + LangChain + Streamlit)

This is a **local, privacy-friendly general knowledge chatbot** built using:

- **Mistral**: A powerful open-source language model
- **Ollama**: To serve the Mistral model locally on your machine
- **LangChain**: To enable memory and conversation handling
- **Streamlit**: For the interactive web user interface (UI)

The chatbot remembers what you’ve asked it during the current session without displaying previous messages. For example, you can say:

> “Who is Narendra Modi?”  
> then ask  
> “What is his age?”  

And the chatbot will know you're referring to Modi.

---

## ⚙️ Tech Stack Breakdown

| Component | Purpose |
|----------|---------|
| **Streamlit** | Creates the web app interface |
| **Ollama** | Runs the local `mistral` model |
| **LangChain** | Adds conversation memory and model management |
| **ConversationBufferMemory** | Remembers the current chat session |
| **Mistral via Ollama** | Generates the actual answers |

---

## 💬 How It Works

This chatbot uses **LangChain's `ConversationBufferMemory`** to remember what the user has asked in previous messages **without showing it in the chat UI**.

LangChain’s `ConversationChain` combines:
- the LLM (`Ollama` model)
- the memory (`ConversationBufferMemory`)

Together, they enable **multi-turn conversations**.

---

▶️ How to Run It
🛠 Requirements
Python 3.10+

Ollama installed on your machine

mistral model pulled locally

🧪 Example Conversation
You: Who is Narendra Modi?
Bot: Narendra Modi is the Prime Minister of India...
You: What is his age?
Bot: Narendra Modi was born on September 17, 1950...

🔁 It remembers the subject of previous messages in the session using ConversationBufferMemory.

🧑‍💻 Author
Built by Harshita ✨
Learning and building in the field of Data Science.
