
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Mafia Wallpaper Bot conectado: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply("Mafia Wallpaper Bot está online!")

if TOKEN:
    bot.run(TOKEN)
else:
    print("Token do Discord não configurado.")
  
