print("o==================================================o")
print("|/------------------------------------------------\|")
print("||     |Python 3 Discord License Distributor|     ||")
print("||     -------\Created by Jayson Fong/-------     ||")
print("|\------------------------------------------------/|")
print("o==================================================o")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import string
import os
import json
debug = False
cooldownSeconds = 30
cooldownAttempts = 1
stockCooldownSeconds = 3
stockCooldownAttempts = 1
logChannelId = None
gameName = None
with open (os.path.dirname(os.path.realpath(__file__)) + "/config/config.json", 'r') as data:
	dataset = json.load(data)
	prefix = dataset['prefix']
	token = dataset['token']
	storage = dataset['storage']
	advanced = dataset['advanced']
	if advanced == '1':
		cooldownSeconds = dataset['cooldownSeconds']
		cooldownAttempts = dataset['cooldownSeconds']
		stockCooldownSeconds = dataset['stockCooldownSeconds']
		stockCooldownAttempts = dataset['stockCooldownAttempts']
		if dataset['logging'] == '1':
			logChannelId = dataset['logging']
		if not dataset['gameName'] == None:
			gameName = dataset['gameName']
data.close()
client = commands.Bot(command_prefix=prefix)
@client.event
async def on_ready():
	print("Logged in as " +  client.user.name + " with client id of " + client.user.id)
	if not gameName == None:
		await client.change_presence(game=discord.Game(name=gameName))
@client.command(pass_context = True)
@commands.cooldown(cooldownAttempts, cooldownSeconds, commands.BucketType.user)
async def request(ctx):
	if not os.stat(storage).st_size == 0:
		with open(storage, 'r') as licenses:
			message = "Here is your license: `" + licenses.readline() + "`"
		with open(storage, 'r') as r:
			next(r)
			data = ""
			for line in r:
				data = data + line
			with open(storage, 'w') as w:
				w.write(data)
			await client.send_message(ctx.message.author, message)
			await client.delete_message(ctx.message)
		if logChannelId is not None:
			message = "<@{0.message.author.id}> ({0.message.author.id} => {0.message.author.name}) has recieved license `" + licenses.readline() + "`"
			await client.send_message(client.get_channel(logChannelId), accountMessageSend.format(ctx))
		licenses.close()
	else:
		print("Warning: Out of Stock; Refill in \"" + storage + "\"")
	await client.send_message(ctx.message.author, "Sorry, we are currently out of stock on licenses. Please try again later.")
@client.command(pass_context = True)
@commands.cooldown(stockCooldownAttempts, stockCooldownSeconds, commands.BucketType.user)
async def stock(ctx):
	with open(storage) as stockcheck:
		stock = len(w.readlines())
	stockcheck.close()
	await client.send_message(ctx.message.author, "We currently have {0} licenses in stock.".format(stock))
	await client.delete_message(ctx.message)
@client.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		await client.send_message(ctx.message.author, "Sorry, this command is currently on cooldown. Please try again in {0} seconds.".format(error.retry_after))
		await client.delete_message(ctx.message)
	if debug == True:
		raise error
client.run(token)
