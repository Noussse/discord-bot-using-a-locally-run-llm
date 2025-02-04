# 🤖 Discord Bot with Ollama AI Integration

This project is a Discord bot that interacts with users, generates responses using the Ollama AI model (such as "llama 3.2"), and manages a dynamic conversation history. The bot maintains context by utilizing a JSON file for user identities.

## ✨ Features

- 📂 **JSON-based Identities**: Stores information related to users, like their personalities or traits, for better AI responses.
- 🧠 **Short Term Memory Model**:
  - 🔄 **Sliding Window Memory**: Retains only the most recent 100 interactions.
  - 📋 **Organized Data**: Each memory includes a unique ID, message, response, and timestamp.
  - 🗑️ **Automatic Purging**: Ensures memory remains within capacity by removing the oldest entries when full.

## ⚙️ Installation & Setup

### Install Required Packages

1️⃣ Install an LLM module from [Ollama](https://ollama.com/search).

2️⃣ Set up the Discord bot and put the token in an `.env` file under the name `DISCORD_TOKEN`.

3️⃣ Ensure you have all the necessary Python dependencies. You can install them via `pip` by running the following command:

```bash
pip install discord ollama requests python-dotenv
```

4️⃣ Preferably, create an `identities.json` file to identify some people on Discord and their personalities for better responses.

📌 **Example for the JSON file:**

```json
{
  "id": {
    "123456789012345678": "name1 is the one who sent this message",
    "987654321098765432": "name2 is the one who sent this message"
  },
  "discord_user_descriptions": "name1 is a passionate coder who loves solving complex problems and building cool projects. name2 is a creative artist with a strong interest in web development and user experience design."
}
```

5️⃣ (Optional) Customize the bot and give it a name using the [Ollama Model File](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#message).

📌 In my script, you will notice it's named **Sage**. If you don't do this step, change the name to match your LLM module name.
