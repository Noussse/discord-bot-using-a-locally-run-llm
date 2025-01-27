# Discord Bot with Ollama AI Integration

This project is a Discord bot that interacts with users, generates responses using the Ollama AI model (such as "llama 3.2"), and manages a dynamic conversation history. The bot maintains context by utilizing a JSON file for user identities.

## Features
- **Ollama AI Integration**: you can use a modelfile to customise your ai.
- **Customizable System Messages**: The bot uses a personalized system message that defines its behavior.
- **JSON-based Identities**: Stores information related to users, like their personalities or traits, for better AI responses.


## Installation & Setup

### 1. Install Required Packages
1-first install an llm module from [ollama](https://ollama.com/search).

2-Set Up Discord Bot and put the token in an env file under the name "DISCORD_TOKEN"

3-ensure you have all the necessary Python dependencies. You can install them via `pip` by running the following command:

```bash
pip install discord ollama requests python-dotenv
```
4-Preferably, you need to create an identities.json file to identify some people on Discord and their personalities for better responses.

example for the jason file :
```bash
  {
  "123456789012345678":  "name1 A passionate coder who loves solving complex problems and building cool projects.",
  "987654321098765432":  "name2 A creative artist with a strong interest in web development and user experience design."
}
```
5-optinally you can customise the bot and give it a name like this  [Ollama Model File](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#message).

In my script, you will notice it's named sage. If you don't do this step, change the name to match your LLM module name.
