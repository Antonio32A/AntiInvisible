import json
import os
import discord
import asyncio

class Handlers:
    class JSON:
        def __init__(self, bot):
            self.bot = bot

        def read():
            with open('data.json', 'r', encoding="utf8") as file:
                data = json.load(file)
            return data

        def dump(data):
            with open('data.json', 'w', encoding="utf8") as file:
                    json.dump(data, file, indent=4)

        def settings_setup(bot):
            if not "data.json" in os.listdir('./'):
                os.system('touch data.json')
            else:
                return
            token = os.getenv('token')
            if token == None:
                token = str(input("Please paste bot's token here (again): "))
            role_id = int(input("Please paste the role id here: "))
            guild_id = int(input("Please paste the guild id here: "))

            with open('data.json', 'w', encoding="utf8") as file:
                data = {
                    "settings": {
                        "token": token,
                        "role_id": role_id,
                        "guild_id": guild_id
                    }
                }
                json.dump(data, file, indent=4)
