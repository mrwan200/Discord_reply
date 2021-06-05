import discord
import pymongo
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

# Setup
CHANNEL_ID = 839863432374911046
TOKEN = "ODAxMzY5NTIyOTA4OTU0NjU0.YAfrhg.............."
PREFIX = "Q:"
MONGODB_URL = "mongodb://localhost:27017/"

# Connect DB
db = pymongo.MongoClient(MONGODB_URL)

# Ready
@bot.event
async def on_ready():
    print("READY!")

# Message
@bot.event
async def on_message(msg):
    if msg.channel.id == CHANNEL_ID:
        if msg.reference:
            collection = db["discord_reply"]["reply"]
            if collection.find_one({"msgid": str(msg.reference.message_id)}):
                print("OK")
                collection.update_one({
                    "msgid": str(msg.reference.message_id),
                },
                {
                    "$push": {
                        "reply": {
                            "msgid": str(msg.id),
                            "msg": msg.content
                        }
                    }
                })
                
        elif msg.content[0:2] == PREFIX:
            collection = db["discord_reply"]["reply"]
            if not collection.find_one({"msgid": str(msg.id)}):
                collection.insert_one({
                    "msgid": str(msg.id),
                    "msg": msg.content.split(PREFIX + " ")[-1],
                    "reply": []
                })

bot.run(TOKEN)