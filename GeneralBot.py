import discord
import datetime
from discord.ext import commands, tasks
from dataclasses import dataclass

Bot_Token = "MTA0Njg3MzYxMTM1ODcyMDA0MA.Gvx3vS.PLoZYYeZ5TYUVqOgYPQx7C7PEAKKEeVZwDxVMs"
Channel_ID = 1046874399233544296
MAX_SESSION_TIME_MINUTES = 15


@dataclass
class Session:
  is_active: bool = False
  start_time: int = 0


bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
session = Session()

#intents = discord.Intents.default()
#intents.message_content = True

@bot.event
async def on_ready():
  print("Hello! The Bot Is Ready!")
  channel = bot.get_channel(Channel_ID)
  await channel.send('Hello! Im Ready:)')


@bot.command()
async def start(ctx):
  if session.is_active:
    await ctx.send("A session is already active!")
    return

  session.is_active = True
  session.start_time = ctx.message.created_at.timestamp()
  human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
  break_reminder.start()
  await ctx.send(f"New session started at {human_readable_time}")

@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():

    # Ignore the first execution of this command.
    if break_reminder.current_loop == 0:
        return

    channel = bot.get_channel(Channel_ID)
    await channel.send(f"**Bro Take a break!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes.")

@bot.command()
async def end(ctx):
  if not session.is_active:
    await ctx.send("No session is active!")
    return

  session.is_active = False
  end_time = ctx.message.created_at.timestamp()
  duration = end_time - session.start_time
  human_readable_duration = str(datetime.timedelta(seconds=duration))
  break_reminder.stop()
  await ctx.send(f"Session ended after {human_readable_duration}.")


@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")


@bot.command()
async def add(ctx, *arr):
  result = 0
  for i in arr:
    result += int(i)

  await ctx.send(f"Result = {result}")


bot.run(Bot_Token)