# bot_test_1.py
from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

# For read the .env file

# For connecting to discord

# Dot env read
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a Bot
bot = discord.Client()

# Handle the on ready event


@bot.event
async def on_ready():
    print(f'{bot.autoM} has connected to Discord!')

# Run the bot with out secret token
bot.run(TOKEN)
