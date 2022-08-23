import discord
from discord.ext import commands
import json
import os

f = open('config.json', "r")
token = json.loads(f.read())  # config.json has the token as a string

bot = commands.Bot(command_prefix=commands.when_mentioned_or(">"))

@bot.event
async def on_ready():
    print("The bot is online.")

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])

bot.run(token)
