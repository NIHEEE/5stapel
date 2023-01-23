import discord

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

    if 'drachen' in message.content:
        await message.channel.send(' lord')

client.run('MTA2NzExNTgzNTEwMzEyOTcxMQ.GNNQRK.PMnIGcHHoc6c6_bmWOJvL4_nSEVVd750-baYJM')


