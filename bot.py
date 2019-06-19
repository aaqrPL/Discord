$ python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip

import discord

TOKEN = 'NTkwODMwMTg1MTM0NDI0MDY0.XQoBqw.CE_UZ1Rnt7_WHuFQYY22xx34mLw'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
