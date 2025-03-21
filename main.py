import settings
import discord
from discord import app_commands
from discord.ext import commands
from cmds.commands import Core

logger = settings.logging.getLogger('bot')

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)
    # Removed explicit creation of CommandTree
    # tree = app_commands.CommandTree(bot)
    
    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')
        logger.info("Loading packages...")
        await bot.add_cog(Core(bot))
        logger.info("Packages loaded successfully.")

    @bot.command(name="list_cogs", help="Lists all loaded cogs")
    async def list_cogs(ctx):
        cogs = list(bot.cogs.keys())
        await ctx.send(f"Loaded cogs: {', '.join(cogs)}")
        
    @bot.command(name="sync", help="Syncs the command tree")
    async def sync(ctx):
        await bot.tree.sync(guild=discord.Object(id=settings.GUILDS_ID))
        await ctx.send("Command tree synced.")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == '__main__':
    run()
