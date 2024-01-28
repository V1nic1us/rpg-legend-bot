import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
token = os.getenv('TOKEN')


@bot.event
async def on_ready():
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send('O bot iniciou!')


bot.run(token)
