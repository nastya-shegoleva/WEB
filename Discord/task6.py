import discord
from discord.ext import commands
import asyncio
import pymorphy2
from translate import Translator

HELP_TEXT = """
!!set_lang сменить язык (пример `!!set_lang ru-en`)
!!text выполнить перевод (пример `!!text привет`)
!!help_bot показать это сообщение
"""

to_lang = dict()
from_lang = dict()
BOT_TOKEN = 'MTIyMjIyODIyNDg4NTM5NTQ3Ng.G9KazS.vu7AUCue1KL4KjbzVZMtwsj20SNa6ZNNcxieFM'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


def default_value(lang):
    if lang not in to_lang:
        to_lang[lang] = 'en'
    if lang not in from_lang:
        from_lang[lang] = 'ru'


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_lang')
    async def set_lang(self, channel, option):
        author = channel.author
        default_value(author)
        lang = option.split('-')
        to_lang[author] = lang[0]
        from_lang[author] = lang[1]
        await channel.send('Настройки сохранены')

    @commands.command(name='text')
    async def text(self, channel, *words):
        author = channel.author
        default_value(author)
        text = ' '.join(words)
        translator = Translator(to_lang=to_lang[author], from_lang=from_lang[author])
        trnsl = str(translator.translate(text))
        await channel.send(trnsl)

    @commands.command(name='help_bot')
    async def text(self, channel):
        await channel.send(HELP_TEXT)


bot = commands.Bot(intents=intents, command_prefix='!!')


async def main():
    await bot.add_cog(Translate(bot))
    await bot.start(BOT_TOKEN)


asyncio.run(main())
