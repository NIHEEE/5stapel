import discord
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    test = message.lower()
    prin(test)
    if 'drachen' in message.content:
        await message.channel.send(' lord')

client.run("MTA1MzgxOTExNTIyOTQyNTgwNg.GOqe1e.b1-nkJpgtlpQga6t6F3_jpwiPE1CHP3M7CjJPA")





