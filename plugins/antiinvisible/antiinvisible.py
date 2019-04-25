import discord
from discord.ext import commands
import os
import time
from util import Handlers

class AntiInvisible(commands.Cog, name="AntiInvisible"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # getting the guild and the role
        guild = discord.utils.get(self.bot.guilds, id=Handlers.JSON.read()["settings"]["guild_id"])
        role = discord.utils.get(guild.roles, id=Handlers.JSON.read()["settings"]["role_id"])

        # is the member in the correct guild or a bot
        if after.bot:
            return
        if not after in guild.members:
            return
        # adding or removing the roles based on their status
        if not (after.status == discord.Status.invisible or after.status == discord.Status.offline):
            try:
                return await after.remove_roles(role)
            except:
                pass
        else:
            try:
                await after.add_roles(role)
            except:
                pass
