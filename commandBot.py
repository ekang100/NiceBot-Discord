import os
import discord
import random
from discord.ext import commands
from keep_alive import keep_alive

activity = discord.Game(name="ur mom")
bot = commands.Bot(command_prefix="$", activity=activity)

print("commandBot works")

# lists for compliment and roast commands
compliments = ["so smart", "pretty", "hot", "very cool", "biswaranjan-level", "amazing", "so funny", "the funniest mf in the world", "crazy", "the best", "sexy af"]

roasts = ["stupid", "mean", "a bully", "boring", "lame", "racist", "sexist", "ugly", "yucky", "smelly", "small dick energy", "slow", "an npc", "a loser"]

#@bot.event
# prints in console when bot is ready
#async def on_ready():
#  print("We have logged in as {0.user}".format(bot))

ccpRoleId = '<@&904767274131529738>'
karemRoleId = '<@&904767810427838495>'

# messages "@ccp is the greatest" when '$eric' is sent
# ccp stands for creamcheesepotato
async def ericImport(ctx):
  await ctx.channel.send(ccpRoleId + " is the greatest")

# messages "@karem kares" when '$karen' is sent
async def karenImport(ctx):
  await ctx.channel.send(karemRoleId + " kares")

# replies "good morning @specified_user or @author if no specification"
async def morningImport(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"Good morning {ctx.message.author.mention}!")
  else:
    await ctx.send(f"Good morning {member.mention}!")

# sends a compliment from list compliments; pings yourself if nobody else is specified, or pings specified member
async def complimentImport(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"{ctx.message.author.mention} says that they are {random.choice(compliments)}")
  else:
    await ctx.send(f"{ctx.message.author.mention} says that {member.mention} is {random.choice(compliments)}")



# same as compliment command but sends a roast instead
async def roastImport(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
    await ctx.channel.send(f"{ctx.message.author.mention} says that they are {random.choice(roasts)}")
  else:
    await ctx.send(f"{ctx.message.author.mention} says that {member.mention} is {random.choice(roasts)}")

# says "pong" in response to ping command
async def pong(ctx):
	await ctx.channel.send("pong")



# slaps a pinged member if specified, slaps author if not specified
#@commands.cooldown(1, 2, commands.BucketType.user)
async def slapImport(ctx, member:discord.User=None):
  if (member == ctx.message.author or member == None):
      await ctx.send(f"{ctx.message.author.mention} slaps themselves!") 
  else:
      await ctx.send(f"{ctx.message.author.mention} slaps {member.mention}!")

# keeping the bot online and obtaining secret token to make it run
keep_alive()
#token = os.environ['TOKEN']
#bot.run(token)