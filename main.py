import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import random

# giving the bot a status
activity = discord.Game(name="ur mom")
bot = commands.Bot(command_prefix="$", activity=activity)

# lists for compliment and roast commands
compliments = ["so smart", "pretty", "hot", "very cool", "biswaranjan-level", "amazing", "so funny", "the funniest mf in the world", "crazy", "the best", "sexy af"]

roasts = ["stupid", "mean", "a bully", "boring", "lame", "racist", "sexist", "ugly", "yucky", "smelly", "small dick energy", "slow", "an npc", "a loser"]


@bot.event
# prints in console when bot is ready
async def on_ready():
  print("We have logged in as {0.user}".format(bot))


@bot.event
# sends "so tru" or "morning @author" depending on message given
async def on_message(message):
  if message.content == "tru" or message.content == "Tru":
    await message.channel.send('so tru')
  if message.content == "morning":
    await message.channel.send(f"good morning {message.author.mention}!")
  if message.content == "bis" or message.content == "Bis" or message.content == "BIS":
    await message.channel.send('Dr. Biswaranjan Pani PhD is the greates human being to ever exist. In the future he will be supreme dictator of the Milky Way Galaxy. He mentors Mr. Kyre Coaker but his best friend is Ryan DCunha')
  await bot.process_commands(message)


ccpRoleId = '<@&904767274131529738>'
karemRoleId = '<@&904767810427838495>'

@bot.command(brief="says ccp is the greatest")
# messages "@ccp is the greatest" when '$eric' is sent
# ccp stands for creamcheesepotato
async def eric(ctx):
  await ctx.channel.send(ccpRoleId + " is the greatest")


@bot.command(brief="says karem kares")
# messages "@karem kares" when '$karen' is sent
async def karen(ctx):
  await ctx.channel.send(karemRoleId + " kares")


@bot.command(brief="Says good morning")
# replies "good morning @specified_user or @author if no specification"
async def morning(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"Good morning {ctx.message.author.mention}!")
  else:
    await ctx.send(f"Good morning {member.mention}!")


@bot.command(brief="Compliment yourself or @ another member")
# sends a compliment from list compliments; pings yourself if nobody else is specified, or pings specified member
async def compliment(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"{ctx.message.author.mention} says that they are {random.choice(compliments)}")
  else:
    await ctx.send(f"{ctx.message.author.mention} says that {member.mention} is {random.choice(compliments)}")


@bot.command(brief="Roast yourself or @ another member")
# same as compliment command but sends a roast instead
async def roast(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"{ctx.message.author.mention} says that they are {random.choice(roasts)}")
  else:
    await ctx.send(f"{ctx.message.author.mention} says that {member.mention} is {random.choice(roasts)}")


@bot.command(brief="Says pong")
# says "pong" in response to ping command
async def ping(ctx):
	await ctx.channel.send("pong")


@bot.command(brief="Slaps yourself or @ another member")
# slaps a pinged member if specified, slaps author if not specified
@commands.cooldown(1, 2, commands.BucketType.user)
async def slap(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
      await ctx.send(f"{ctx.message.author.mention} slaps themselves!") 
  else:
      await ctx.send(f"{ctx.message.author.mention} slaps {member.mention}!")


# keeping the bot online and obtaining secret token to make it run
keep_alive()
token = os.environ['TOKEN']
bot.run(token)