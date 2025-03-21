import discord
from discord.ext import commands
import settings

logger = settings.logging.getLogger(__name__)



class TemporaryVoice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        possible_channel_name = f"{member.nick}'s plekje"
        if after.channel:
            if after.channel.name == "🔊 [ Join to Create ] 🔊":
                temp_channel = await after.channel.clone(name=possible_channel_name)
                await member.move_to(temp_channel)
                self.temporary_channels.append(temp_channel.id)
        if before.channel:
            if before.channel.id in self.temporary_channels:
                if len(before.channel.members) == 0:
                    await before.channel.delete()
async def setup(bot):
    await bot.add_cog(TemporaryVoice(bot))