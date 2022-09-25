from discord.ext import commands


class Conversions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def fahrenheit(self, ctx, n):
        fahr = round((float(n) * (9/5)) + 32, 2)
        await ctx.send(f"{fahr}°F")


    @commands.command()
    async def celsius(self, ctx, n):
        cels = round((float(n) - 32) * (5/9), 2)
        await ctx.send(f"{cels}°C")



async def setup(bot):
    await bot.add_cog(Conversions(bot))