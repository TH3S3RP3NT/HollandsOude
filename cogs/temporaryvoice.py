import discord
from discord.ext import commands
import settings

logger = settings.logging.getLogger(__name__)



class TemporaryVoice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        possible_channel_name = f"{member.nick} 's plekje"
        if after.channel.name == 'Creeer je eigen VC':
            temp_channel = await after.channel.clone(name=possible_channel_name)
            await member.move_to(temp_channel)
        if before.channel.name == possible_channel_name:
            if len(before.channel.members) == 0:
async def setup(bot):
    await bot.add_cog(TemporaryVoice(bot))