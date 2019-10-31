import discord
from discord.ext import commands
import os
import json
import asyncio
import aiohttp
import random
from util.handlers import Handlers

class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def update_activity(self):
        await self.change_presence(status=discord.Status.online)


    async def load_plugins(self):
        plugins = ["owner", "antiinvisible", "typingrole"]
        for plugin in plugins:
            self.load_extension(f"plugins.{plugin}")
            print(f"Loaded {plugin}.")
        print("Starting...")


    async def on_ready(self):
        print("Starting...")
        await self.load_plugins()
        await self.update_activity()
        print(f"Logged in as {self.user} ({self.user.id})")
        print("Created by: Antonio32A (https://github.com/Antonio32A)")
