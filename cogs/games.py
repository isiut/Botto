from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def rps(self, ctx, *, user_choice):
        user_choice = user_choice.lower()

        beats = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        rps_emojis = {
            "rock": "🗿",
            "paper": "🧻",
            "scissors": "✂️"
        }

        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            await ctx.send(f"It's a draw!\nThe computer chose {computer_choice}\n{rps_emojis[user_choice]} = {rps_emojis[computer_choice]}")

        elif user_choice == beats[computer_choice]:
            await ctx.send(f"You lost!\nThe computer chose {computer_choice}\n{rps_emojis[user_choice]} < {rps_emojis[computer_choice]}")

        elif computer_choice == beats[user_choice]:
            await ctx.send(f"You won!\nThe computer chose {computer_choice}\n{rps_emojis[user_choice]} > {rps_emojis[computer_choice]}")

        else:
            await ctx.send(f"Error, {computer_choice}")
            
            
        



def setup(client):
    client.add_cog(Games(client))