import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("_____________")

    bot = commands.Bot(command_prefix='!', intents=intents)

if __name__ == '__main__':
    run()