# This is basically the first iteration where we have a working bot

import discord
from discord.ext import commands

# Bot command
client = commands.Bot(command_prefix = '$start')

# Denotes an event
@client.event

# When the bot is in a ready normal state do this
async def on_ready():
    print("Hello Everyone I am PersOna!")

# Runs the bot and please put in Bot TOKEN
client.run('')