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
import config.language
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
	print(config.language.start_msg.format(client.user.name, client.user.id))
	if not gameName == None:
		await client.change_presence(game=discord.Game(name=gameName))
@client.command(pass_context = True)
@commands.cooldown(cooldownAttempts, cooldownSeconds, commands.BucketType.user)
async def request(ctx):
	if not os.stat(storage).st_size == 0:
		with open(storage, 'r') as licenses:
			message = config.language.license_provide + "`" + licenses.readline() + "`"
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
			message = config.language.license_log.format(licenses.readline())
			await client.send_message(client.get_channel(logChannelId), message.format(ctx))
		licenses.close()
	else:
		print(config.language.stock_depleted_console.format(storage))
	await client.send_message(ctx.message.author, config.language.stock_depleted)
@client.command(pass_context = True)
@commands.cooldown(stockCooldownAttempts, stockCooldownSeconds, commands.BucketType.user)
async def stock(ctx):
	with open(storage) as stockcheck:
		stock = len(stockcheck.readlines())
	stockcheck.close()
	await client.send_message(ctx.message.author, config.language.stock_check.format(stock))
	await client.delete_message(ctx.message)
@client.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		await client.send_message(ctx.message.author, config.language.cooldown_error.format(error.retry_after))
		await client.delete_message(ctx.message)
	if debug == True:
		raise error
client.run(token)
