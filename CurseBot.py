import discord
from discord.ext import commands

Bot_Token = "MTA0Njg5Njc5MzExMzMyOTc0NQ.GKcyhK.oJS_79V7OXpe9OtdCI522XhGDITRFyV2_80S7o"
bot = commands.Bot(command_prefix='', intents=discord.Intents.all())
Channel_ID = 1046874399233544296


@bot.event
async def on_ready():
  print("The Bot Is Ready")
  channel = bot.get_channel(Channel_ID)
  await channel.send('Why are you here???')


@bot.command()
async def fuckyou(ctx):
  await ctx.send("Fuck you")

@bot.command()
async def fuck(ctx):
  await ctx.send("no fuck you")

@bot.command()
async def shit(ctx):
  await ctx.send("shit yourself bitch")


@bot.command()
async def yourself(ctx):
  await ctx.send("kill yourself")


@bot.command()
async def dumb(ctx):
  await ctx.send("you dumb motherfucker")


@bot.command()
async def cringe(ctx):
  await ctx.send("look who's talking")


@bot.command()
async def wtf(ctx):
  await ctx.send("hahahaha not funny commit scuicide please")


bot.run(Bot_Token)