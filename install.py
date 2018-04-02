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
print("o==================================================o")
print("|/------------------------------------------------\|")
print("||     |Python 3 Discord License Distributor|     ||")
print("||     -------\Created by Jayson Fong/-------     ||")
print("||             \----\Installing/----/             ||")
print("|\------------------------------------------------/|")
print("o==================================================o")
if token.lower() == "n":
        token = "TOKEN"
newdata = {'token': token, 'storage': storage, 'prefix': prefix}
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
