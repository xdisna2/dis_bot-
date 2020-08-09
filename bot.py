# This is basically the first iteration where we have a working bot

import discord
from discord.ext import commands

# Bot command
client = commands.Bot(command_prefix = '$')

# Denotes an event
@client.event
# When the bot is in a ready normal state do this
async def on_ready():
    print("Hello Everyone I am PersOna!")

# Client bot has connected to discord
@client.event
async def on_connect():
    print("Connected to Discord...")

# Greets someone that has joined the server
@client.event
async def on_member_join(member):
    print(f'{member} has joined the testing server.')

# Tells us that a user has been banned or left the server
@client.event
async def on_member_remove(member):
    print(f'{member} has been BANISHED TO THE SHADOW REALM')

# Upon using $convo command, sends a message
@client.command()
async def convo(ctx):
    await ctx.send('Hello there!')
    await ctx.send(f'My Latency is {round(client.latency * 1000)}ms ')

# Runs the bot and please put in Bot TOKEN
client.run('NzMxNjcxNTUxMDk5MDExMDgy.XwpcOw.mBvQatZBpVN4ZC56SawIobNfe5s')