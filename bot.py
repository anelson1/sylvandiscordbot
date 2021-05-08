import discord 
import os

bot = discord.Client()

@bot.event
async def on_ready():
    print("Bot is ready")
@bot.event
async def on_message(message):
    if message.content.lower() == "!hello":
        await message.channel.send("Hello World!")
    if "!echo" in message.content.lower():
        await message.channel.send(message.content[6::])
bot.run(os.environ['bot_key'])
