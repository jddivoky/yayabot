import os
print("After os import")
import discord
print("After discord import")
from discord.ext import commands
print("After commands import")
from discord import app_commands
print("After app_commands import")

# Retrieve the bot token from environment variables for security
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
print("After TOKEN setup")

# Define intents for your bot.
# discord.Intents.default() provides common intents.
# discord.Intents.message_content is often required for reading message content.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
print("After intents setup")

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
print("After bot initialization")
print(f"Bot command tree before tree initialization: {getattr(bot, 'tree', 'No tree attribute')}")

# Add a Tree object for synchronizing slash commands
#print("Before CommandTree initialization (Line 21)")
# **Create your own help command:** Define a new command with the name `help` using the `@bot.command()` decorator. Inside this command function, you can manually create and send the help message using `await ctx.send()` or by embedding the information in a more visually appealing way using `discord.Embed`.

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print("Inside on_ready")
    print(f'{bot.user.name} has connected to Discord!')
    print('Bot is ready to receive messages and commands.')
#    await ctx.send("YayaBot is online!")

# Disable the default help command when initializing the bot
# bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# ... rest of your code ...

# **Create your own help command:** Define a new command with the name `help` using the `@bot.command()` decorator. Inside this command function, you can manually create and send the help message using `await ctx.send()` or by embedding the information in a more visually appealing way using `discord.Embed`.
# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Bot is ready to receive messages and commands.')
#    await ctx.send("YayaBot is online!")

# Disable the default help command when initializing the bot

@bot.command(name='help')
async def custom_help(ctx, command_name: str = None):
    """Shows help for commands and triggers."""

    if command_name:
        # Help for a specific command
        command = bot.get_command(command_name)
        if command:
            help_message = f"**{command.name}:** {command.help}"
            await ctx.send(help_message)
        else:
            await ctx.send(f"Command '{command_name}' not found.")
    else:
        # General help message
        help_message = "**Available Commands:**\n"
        for command in bot.commands:
            help_message += f"- `{bot.command_prefix}{command.name}`: {command.help or 'No description'}\n"

        # Manually list your triggers
        help_message += "\n**Available Triggers:**\n"
        help_message += "- yaya\n"
        help_message += "- dismaya\n"
        help_message += "- smo\n"
        help_message += "- please\n"
        help_message += "- bruh\n"
        help_message += "- fried rice friday\n"
        # Add other triggers here as you create them

        await ctx.send(help_message)

# Removed @bot.command()
@app_commands.command(name='restart', description='Restarts the bot (admin only).')
async def restart(interaction: discord.Interaction): # Changed function signature
    """Restarts the bot (admin only)."""
    allowed_user_id = 978055148091867157  # Your Discord user ID

    if interaction.user.id == allowed_user_id: # Changed how to get user ID
        # Use interaction.response.send_message for slash command responses
        await interaction.response.send_message("Restarting bot...")
        # Here you would add the actual code to restart your bot.
        import sys
        import os
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        # Use interaction.response.send_message for slash command responses
        await interaction.response.send_message("You do not have permission to restart the bot.", ephemeral=True) # Added ephemeral=True


# Command: A simple 'hello' command
@app_commands.command(name='hello', description='Responds with a greeting.')
async def hello(ctx):
    """Responds with a greeting."""
    await ctx.send(f'Hello, {ctx.author.name}! I am {bot.user.name}.')

# Command: A simple 'ping' command
#@bot.command()
    """Responds with 'Pong!' and bot latency."""
    latency = round(bot.latency * 1000) # Convert latency to milliseconds

# time
#@bot.command()
@app_commands.command(name='time', description='Displays the current time.')
async def time(ctx):
    """Displays the current time."""
    await ctx.send("time = time_right_now")


# Event: Every time a message is received
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Process commands first. If this message is a command,
    # bot.process_commands will handle it and we can return early.
    await bot.process_commands(message)

    # If the message was a command, we stop processing here to avoid
    # triggering other on_message logic for commands.
    if message.content.startswith(bot.command_prefix):
        return

    # If the message is not a command, continue with other on_message logic.
    # Check if the message contains the word "yaya" (case-insensitive)
    if "yaya" in message.content.lower():
        await message.channel.send("https://c.tenor.com/3ZHycWSm69oAAAAd/tenor.gif")
    # dismaya
    if "dismaya" in message.content.lower():
        await message.channel.send("https://static.wikia.nocookie.net/png-phobia/images/7/7c/Flab.png/revision/latest/thumbnail/width/360/height/360?cb=20240228215811")
    # smo
    if "smo" in message.content.lower():
        await message.channel.send("smeef")
    # please
    if "please" in message.content.lower():
        await message.channel.send("pees*")
    # bruh
    if "bruh" in message.content.lower():
        await message.channel.send('hmm... yes that is indubitably "bruh" worthy')
    # FRIED RICE FRIDAY!!!
    if "fried rice friday" in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/1235025733106012261/1362595167386996736/images.png?ex=6802f723&is=6801a5a3&hm=e30ac9d43bab72f05fcf011a1b9303acc66410240029c5b899c978eecadc3eee&')
    # hurb
    if "indubitably" in message.content.lower():
        await message.channel.send("indubitabubitably")
    # indeed
    if "indeed" in message.content.lower():
        await message.channel.send(""""I need [indeed](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRKP8vsj3MfwK1UC9UIOz6BF6o6cRBJ5vNcQ&s)."
[Indeed](https://www.indeed.com/), you do.""")
    # SKULL EMOJI
    if ":skull:" in message.content.lower():
        await message.channel.send("""SKULL EMOJIIIII:bangbang::bangbang:
https://youtu.be/l-UDFCULlzE?si=L71H0wOKCNge7wVG""")
    # SKULL EMOJI
    if "💀" in message.content.lower():
        await message.channel.send("""SKULL EMOJIIIII:bangbang::bangbang:
https://youtu.be/l-UDFCULlzE?si=L71H0wOKCNge7wVG""")
    if "rip arkansas" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/1296624229239881765/1364738893102055571/ezgif.com-animated-gif-maker_4.gif?ex=6814a6e3&is=68135563&hm=66692453525698f13419c3e1ebe04deefd1031f75e4ce8525b657bdff4bb5ab8&")
    # trains
    if "trains" in message.content.lower():
        await message.channel.send("i like trains")
        embed = discord.Embed(
            title="trains",
            description="me gusta los trenes\ni like trains",
            color=discord.Color.green() # Or any color you like
        )
        embed.set_image(url="https://i.imgur.com/mEuGT3g.gif")

        await message.channel.send(embed=embed)
    # nugget gif
    if "<@978055148091867157>" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/1296624229239881760/1338685439602856008/ezgif.com-animated-gif-maker_1.gif?ex=68346eb8&is=68331d38&hm=dcc37c42f7b3a020874f3abadb74aa7ee131482f23530d5c0e5aa448c92503fa&")

    """ TEMPLATE
    if "trigger" in message.content.lower():
        await message.channel.send("response")
    """


    # Add any other non-command message processing logic here.

    # This line is important! It allows your commands (like !ping) to still work
    await bot.process_commands(message)

# New Echo Slash Command (Admin Only)

@bot.tree.command(name='echo', description='Echoes the provided text (admin only).')
@app_commands.describe(text='The text to echo.')
async def echo(interaction: discord.Interaction, text: str):
    """Echoes the provided text (admin only)."""
    allowed_user_id = 978055148091867157  # Your Discord user ID

    if interaction.user.id == allowed_user_id:
        await interaction.response.send_message(text)
    else:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True) # ephemeral=True makes the message only visible to the user who used the command

# Main entry point to run the bot
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