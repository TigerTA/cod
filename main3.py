import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTExNDIyMjY5MzAzMDU3MjEyMw.GN9K9r.SSkNmnNVPnWnD_9_O1HlZGDckuIhwZclnBEt3U")




# name = 'Rafik'
# age = 10
# print('Привет, меня зовут', name, 'и мне', age, 'лет') | print(f'Привет, меня зовут {name} и мне {age} лет')