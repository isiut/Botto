import asyncio
import discord
from discord.ext import commands
import json
import os

# config.json has the token as a string (in .gitignore)
f = open('bot/config.json', "r")
token = json.loads(f.read())

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(">"),
    intents=intents)


@bot.event
async def on_ready():
    print("The bot is online.")
    await bot.change_presence(activity=discord.Game("with the bot"))

async def load_extensions():
    for f in os.listdir("bot/cogs"):
        if f.endswith(".py"):
            await bot.load_extension("cogs." + f[:-3])

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())