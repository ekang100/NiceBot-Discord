import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

activity = discord.Game(name="ur mom")
bot = commands.Bot(command_prefix="$", activity=activity)

#@bot.event
# prints in console when bot is ready
#async def on_ready():
#  print("We have logged in as {0.user}".format(bot))

print("eventBot works")


# sends "so tru" or "morning @author" depending on message given
async def messager(message):
  if message.content == "tru" or message.content == "Tru":
    await message.channel.send('so tru')
  if message.content == "morning":
    await message.channel.send(f"good morning {message.author.mention}!")

  #bis message
  if message.content == "bis" or message.content == "Bis" or message.content == "BIS":
    await message.channel.send('Dr. Biswaranjan Pani PhD is the greates human being to ever exist. In the future he will be supreme dictator of the Milky Way Galaxy. He mentors Mr. Kyre Coaker but his best friend is Ryan DCunha')

#jim message
  if message.content == "Jim" or message.content == "jim" or message.content == "JIM":
    await message.channel.send('WE GO JIM!!!!')
  await bot.process_commands(message)

# keeping the bot online and obtaining secret token to make it run

keep_alive()
#token = os.environ['TOKEN']
#print('t')
#bot.run(token)
#print('l')