import os.path
import sys, traceback
import json
print("o==================================================o")
print("|/------------------------------------------------\|")
print("||     |Python 3 Discord License Distributor|     ||")
print("||     -------\Created by Jayson Fong/-------     ||")
print("|\------------------------------------------------/|")
print("o==================================================o")
if not os.path.isdir(os.path.dirname(os.path.realpath(__file__)) + "/config"):
	print("Error: Could Not Locate Configuration Directory")
	sys.exit(0)
elif os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "/config/config.json"):
	override = input("Configuration Already Exists; Override? (Y|N): ")
	if not override.lower() in ["y", "n"]:
		print("Error: Invalid Input; Defaulting False; Exiting")
		sys.exit(0)
	elif override.lower() == "n":
		print("Cancelling Installation")
		sys.exit(0)
token = input("Discord Token (N|STRING): ")
storage = input("License Storage File (N|STRING): ")
if not os.path.isfile(storage):
	print("Error: Invalid Storage File")
	sys.exit(0)
prefix = input("Discord Bot Command Prefix (STRING): ")
if not prefix:
	print("Error: Invalid Command Prefix; Defaulting to \"!\"")
	prefix = "!"
advanced = input("Complete Advanced Configuration? (Y|N): ")
if advanced.lower() == "y":
	advanced = '1'
	cooldownSeconds = input("License Retrieval Cooldown Seconds: ")
	if not cooldownSeconds:
		print("Error: Invalid Cooldown Seconds; Defaulting to \"30\"")
		cooldownSeconds = 30
	if not int(cooldownSeconds):
		print("Error: Cooldown Must Be Interger")
		sys.exit(0)
	cooldownAttempts = input("License Retrieval Cooldown Attempts per " + str(cooldownSeconds) + " Seconds: ")
	if not cooldownAttempts:
		print("Error: Invalid Cooldown Attempts; Defaulting to \"1\"")
		cooldownAttempts = 1
	if not int(cooldownSeconds):
		print("Error: Cooldown Attempts Must Be Interger")
		sys.exit(0)
	stockCooldownSeconds = input("License Retrieval Cooldown Seconds: ")
	if not stockCooldownSeconds:
		print("Error: Invalid Cooldown Seconds; Defaulting to \"30\"")
		stockCooldownSeconds = 30
	if not int(stockCooldownSeconds):
		print("Error: Cooldown Must Be Interger")
		sys.exit(0)
	stockCooldownAttempts = input("License Retrieval Cooldown Attempts per " + str(stockCooldownSeconds) + " Seconds: ")
	if not stockCooldownAttempts:
		print("Error: Invalid Cooldown Attempts; Defaulting to \"1\"")
		stockCooldownAttempts = 1
	if not int(stockCooldownSeconds):
		print("Error: Cooldown Attempts Must Be Interger")
		sys.exit(0)
	logging = input("Enable License Logging? (Y|N): ")
	if logging.lower() == 'y':
		logChannelId = input("Log Licenses in Channel ID: ")
		if not logChannelId:
			logging = '0'
			logChannelId = "None"
		else:
			logging = '1'
	else:
		logChannelId = "None"
	gameName = input("Bot Game Name (DEFAULT|STRING): ")
	if not gameName:
		gameName = "None"
print("o==================================================o")
print("|/------------------------------------------------\|")
print("||     |Python 3 Discord License Distributor|     ||")
print("||     -------\Created by Jayson Fong/-------     ||")
print("||             \----\Installing/----/             ||")
print("|\------------------------------------------------/|")
print("o==================================================o")
if token.lower() == "n":
	token = "TOKEN"
if advanced == '1':
	newdata = {'token': token, 'storage': storage, 'prefix': prefix, 'cooldownSeconds': cooldownSeconds, 'cooldownAttempts': cooldownAttempts, 'stockCooldownSeconds': stockCooldownSeconds, 'stockCooldownAttempts': stockCooldownAttempts, 'logging': logging, 'logChannelId': logChannelId, 'gameName': gameName, 'advanced': advanced}
else:
	newdata = {'token': token, 'storage': storage, 'prefix': prefix, 'advanced': '0'}
with open (os.path.dirname(os.path.realpath(__file__)) + "/config/config.json", 'w') as config:
	json.dump(newdata, config)
config.close()
print("o==================================================o")
print("|/------------------------------------------------\|")
print("||     |Python 3 Discord License Distributor|     ||")
print("||     -------\Created by Jayson Fong/-------     ||")
print("||             \----\Installed!/----/             ||")
print("|\------------------------------------------------/|")
print("o==================================================o")

