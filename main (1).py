import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

data = ['ЭКОНОМЬТЕ РЕСУРСЫ', 'РАЗДЕЛЯЙТЕ МУСОР', 'СДАВАЙТЕ ВТОРСЫРЬЁ', 'ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ', 'ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ', 'ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ', 'ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ', 'ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx):
    eco_message = random.choice(data)
    await ctx.send(eco_message)

bot.run("ЛОЛ")