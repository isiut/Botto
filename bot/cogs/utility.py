import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gpa(self, ctx, *args):
        if len(args) != 2:
            await ctx.send("Please enter A and B amounts.\nExample: >gpa 35 3")
            return

        try:
            a = int(args[0])
            b = int(args[1])
            gpa = ((a*4)+(b*3))/(a+b)
            gpa = round(gpa, 3)

            await ctx.send(f"Your GPA is {gpa}")
        except:
            await ctx.send("Please enter valid integer A and B amounts.\nExample: >gpa 35 3")

    
    @commands.command()
    async def avi(self, ctx, *, member: discord.Member = None):
        if member is None:
            await ctx.send(ctx.author.avatar_url)
        else:
            av = member.avatar_url
            await ctx.send(av)



def setup(bot):
    bot.add_cog(Utility(bot))
        

