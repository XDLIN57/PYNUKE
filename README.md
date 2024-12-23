It looks like the markdown formatting is being displayed as raw text, likely due to incorrect syntax in your markdown file. Here's how to ensure everything is properly formatted, and I'll clean it up for you:

```markdown
# 🔥 **Pynuke - Discord Server Nuke Bot** 🔥

Pynuke is a **powerful Discord bot** that allows you to test server defenses by **automating chaotic actions** such as **mass DM spamming**, **channel creation**, and **role management**. Fully customizable and easy to use!

---

## 🚀 **Features**

- 💬 **Mass DM Spamming**: Send custom messages to up to **50 users** at once.
- 🔧 **Channel & Role Creation**: Automatically create multiple channels and roles to disrupt the server.
- ⚡ **Message Spamming**: Spam custom messages in various channels for maximum disruption.
- ⚙️ **Customizable**: Personalize messages, channel names, and roles for full control.
- ⏱️ **Rate Limiting**: Handles Discord rate limits smoothly for efficient operation.

---

## 🛠️ **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Pynuke.git
   cd Pynuke
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install required libraries**:
   ```bash
   pip install discord.py colorama
   ```

---

## 🚀 **Usage**

1. **Run the script**:
   After setting up your bot token, simply run the script to start the process.

2. **Configure the script**:
   During setup, you'll be prompted to input:
   - 🔑 **Bot token**
   - 🏙️ **Server ID to nuke**
   - 💌 **Custom messages, channels, and roles**

3. **Start the nuke**:
   The bot will begin by sending mass DMs, creating channels, spamming messages, and managing roles in the server. 🌪️

---

## 💡 **Example Setup**

```bash
Enter bot token: <bot_token> 💻
Enter server ID: <server_id> 🏙️
Enter message 1: "Welcome to chaos!" 🔥
Enter channel name: "spam-channel" 📢
Enter role name: "raider" ⚔️
```

---

## ⚖️ **Legal Notice**

- ⚠️ **For educational purposes only.**
- 🚫 **Do not use on servers without permission.**
- ⚠️ **This script may violate Discord's Terms of Service. Use responsibly.**

---

## 📝 **License**

MIT License - see [LICENSE](LICENSE) for details.

---

## ❤️ **Support**

If you encounter any issues, feel free to open an issue in the GitHub repository. Let's make Pynuke even better! 💪

---

## 🚨 **Update**

- 🚀 **Better Nuking!**: Improved efficiency and better rate limit handling for more effective server disruption.
```

This should now properly render the markdown file with the correct formatting and emojis when viewed on GitHub or a markdown viewer. The key things to note are:

1. **Triple backticks (` ``` `) around code blocks**: This makes the code sections stand out properly.
2. **Headings with hash signs**: `#`, `##`, `###` create different levels of headings.
3. **Proper spacing between sections**: Markdown is very sensitive to spacing for proper rendering.

Try copying this exactly into your `README.md`, and it should render as you expect!
