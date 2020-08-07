# Imports the Discord.py module
import discord

# This is our bot client's connection to Discord itself
client = discord.Client()

# Registers an event
@client.event
# This event is called when the bot logs in and sets things up
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
# When the bot RECEIVES a message
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await  message.channel.send('Hello!')

# Runs the bot with our LOGIN Token
client.run('')