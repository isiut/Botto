from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.bot.latency, 3)
        await ctx.send(f"✅ The latency is {bot_latency}s")



async def setup(bot):
    await bot.add_cog(Info(bot))