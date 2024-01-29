from discord.ext import commands


class BotStarted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(int(self.bot.CHANNEL_ID))
        await channel.send('O bot iniciou!')


async def setup(bot):
    await bot.add_cog(BotStarted(bot))
