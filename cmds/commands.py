import discord
from discord.ext import commands
import settings

logger = settings.logging.getLogger(__name__)


class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="embed_with_buttons", description="Creates an embed with buttons")  # ✅ Correct Slash Command
    async def embed_with_buttons(self, interaction: discord.Interaction):  # ✅ Slash commands use discord.Interaction
        embed = discord.Embed(title="Sample Embed", description="This is an embed with buttons",
                              color=discord.Color.blue())
        view = discord.ui.View()
        button = discord.ui.Button(label="Click Me", style=discord.ButtonStyle.primary)

        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message("Button clicked!", ephemeral=True)

        button.callback = button_callback
        view.add_item(button)

        await interaction.response.send_message(embed=embed,
                                                view=view)  # ✅ Slash commands require response via interaction

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'Cog {self.__class__.__name__} is ready.')


