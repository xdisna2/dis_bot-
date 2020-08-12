# This is basically the first iteration where we have a working bot

import discord
from discord.ext import commands
import random

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

# Create a magical 8 ball command with different aliases that can be accepted for the command invoke
@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['Yes', 'No', 'Maybe']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Clears 5 messages unless otherwise specified
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Runs the bot and please put in Bot TOKEN
client.run('')