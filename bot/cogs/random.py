from discord.ext import commands
import random

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   
    # something wrong with rng command
    @commands.command()
    async def rng(self, ctx, *rng_args):
        if len(rng_args) != 2:
            await ctx.send("Please enter 2 arguments.")
            return

        first = rng_args[0]
        last = rng_args[1]

        if first >= last:
            await ctx.send("The second value has to be greater than the first value.")
        else:
            await ctx.send(random.randint(int(first), int(last)))


    @commands.command()
    async def coinflip(self, ctx):
        coin_choice = random.choice(["Heads", "Tails"])
        await ctx.send(f"It's {coin_choice}!")



async def setup(bot):
    await bot.add_cog(Random(bot))