import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger('bot')

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')


    @bot.command(
        aliases=['p'],
        help="This command is for testing purposes",
        description="This command is for testing purposes",
        brief="testing purposes",
        enable=False,
        hidden=False
    )
    async def ping(ctx):
        await ctx.send('Pong!')

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__ == '__main__':
    run()