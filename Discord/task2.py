import discord
from discord.ext import commands
import random, logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='#!', intents=intents)


@bot.command(name='randint')
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


TOKEN = "MTIyMjIyODIyNDg4NTM5NTQ3Ng.GhMEMC.6gBS2OCQpf7ihW4eLAtdsVZqvN0MyS7QWDj8jo"

bot.run(TOKEN)
