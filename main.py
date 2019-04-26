import discord
from discord.ext import commands
from util import Bot, Handlers
import os

if "data.json" in os.listdir('./'):
    config = Handlers.JSON.read()["config"]
    token = config["token"]
else:
    token = os.getenv('token')

def get_pre(bot, message):
    id = bot.user.id
    l = [f"<@{id}> ", f"<@!{id}> ", "'"]
    return l


bot = Bot(command_prefix=get_pre, owner_id=166630166825664512)

if __name__ == '__main__':
    bot.run(token)
