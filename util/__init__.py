from .bot import Bot
from .handlers import Handlers

async def setup(bot):
    await bot.add_cog(Util(bot))
