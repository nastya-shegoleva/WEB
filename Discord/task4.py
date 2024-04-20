import asyncio
import discord
import re

TOKEN = "BOT_TOKEN"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


class Timer(client):
    def on_ready(self):
        for gield in self.guilds:
            return f'{self.user} поключился к чату {gield.name}(id: {gield.id})'

    async def on_message(self, message):
        h = 0
        m = 0
        message = message.content.lower().split()
        if message.author == client.user:
            return
        if 'hours' in message:
            h = int(message.index('hours')) - 1
        if 'minutes' in message:
            m = int(message.index('minutes')) - 1

        self.loop.create_task(self.time(h * 3600 + m * 60, 'The X time has came!', message.channel))

    async def time(self, time, message, channel):
        await asyncio.sleep(time)
        await channel.send(message)


time = Timer()
time.run(TOKEN)
