import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

CHANNEL_ID = 1234567890123456
TOKEN = "ODAxMzY5NTIyOTA4OTU0NjU0.YAfrhg.KILnfSxrqxeEK8_a_9ogkUp6gIY"
PREFIX = "Q:"

db = []

@bot.event
async def on_ready():
    print("READY!")

@bot.event
async def on_message(msg):
    if msg.channel.id == CHANNEL_ID:
        if msg.reference:
            for x in db:
                if x["msgid"] == str(msg.reference.message_id):
                    x["reply"].append({
                        "id": str(msg.id),
                        "msg": msg.content
                    })

                    print(db)
                
        elif msg.content[0:2] == PREFIX:
            db.append({
                "msgid": str(msg.id),
                "msg": msg.content.split(PREFIX + " ")[-1],
                "reply": []
            })

            print(db)

bot.run(TOKEN)