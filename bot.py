import discord 

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
bot.run('ODM1NTQwNDI1ODg4MzY2NjAz.YIQ7qQ.LlOuMyE21gQIEZ4EV6-fzTEB3C8')
