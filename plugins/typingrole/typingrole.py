import discord
from discord.ext import commands
import asyncio
from util import Handlers

class TypingRole(commands.Cog, name="TypingRole"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        print("typing")
        guild = discord.utils.get(self.bot.guilds, id=Handlers.JSON.read()["config"]["guild_id"])
        role = guild.get_role(Handlers.JSON.read()["config"]["typer_role_id"])
        if not role in user.roles:
            return
        role2 = guild.get_role(Handlers.JSON.read()["config"]["typing_role_id"])
        await user.add_roles(role2)
        await asyncio.sleep(10)
        await user.remove_roles(role2)
