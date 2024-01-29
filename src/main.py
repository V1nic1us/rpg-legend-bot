import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.CHANNEL_ID = os.environ['CHANNEL_ID']
token = os.getenv('TOKEN')


async def load_extensions():
    events_dir = os.path.join(os.path.dirname(__file__), 'events')

    for filename in await asyncio.to_thread(os.listdir, './commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

    for filename in os.listdir(events_dir):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')


async def main():
    await load_extensions()
    await bot.start(token)


asyncio.run(main())
