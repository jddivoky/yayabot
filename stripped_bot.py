import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Bot is ready.')
# Add the run command
if __name__ == '__main__':
    if TOKEN is None:
        print("ERROR: DISCORD_BOT_TOKEN environment variable is not set. The bot cannot start.")
    else:
        try:
            bot.run(TOKEN)
        except discord.LoginFailure:
            print("ERROR: Failed to log in. Check your DISCORD_BOT_TOKEN.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")