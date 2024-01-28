import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from src.services.UserService import create_user, User

load_dotenv()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
CHANNEL_ID = os.getenv('CHANNEL_ID')
token = os.getenv('TOKEN')


@bot.command()
async def start(ctx: commands.Context):
    new_user = User(
        discord_id=ctx.author.id,
        username=ctx.author.name,
        joined_at=ctx.author.joined_at,
        avatar_url=ctx.author.avatar)
    print(new_user)
    # create_user(new_user)
    await ctx.send(f'user {ctx.author} started')


@bot.command(aliases=['p'])
async def profile(ctx: commands.Context):
    await ctx.send(f'profile')


@bot.command()
async def shop(ctx: commands.Context):
    await ctx.send(f'shop')


@bot.command()
async def buy(ctx: commands.Context):
    await ctx.send(f'buy')


@bot.command()
async def sell(ctx: commands.Context):
    await ctx.send(f'sell')


@bot.command(aliases=['inv'])
async def inventory(ctx: commands.Context):
    await ctx.send(f'inventory')


bot.run(token)
