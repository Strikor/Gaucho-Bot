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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, I\'m GauchoBot and I\'m here to help!')

client.run('MTE0OTMzNzQ2NTQ3NjM1NDEwOQ.G_0pQ9.Hp-b2VDuE4dG5xFIC62SPNDW43ZT2quhzryfxc')