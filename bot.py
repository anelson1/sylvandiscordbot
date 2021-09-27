import discord 
import os
import random
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
    print("Bot is ready")
@bot.event
async def on_message(message):
    if message.content.lower() == "!ping":
        await message.channel.send("@"+message.author)
    if message.content.lower() == "!hello":
        await message.channel.send("Hello World!")
    if message.content.lower()[0:6] == "!echo ":
        await message.channel.send(message.content[6::])
    if "!color" in message.content.lower():
        desiredcolor = message.content[7::]
        await message.author.top_role.edit(color = discord.Color.random())
        await message.channel.send("Color Changed to a random color")
    if "!name" in message.content.lower():
        newname = message.content[6::]
        await message.author.top_role.edit(name = newname)
    if "!perm" in message.content.lower():
        perm = message.content[6::]
        if perm == "nickname":
            await message.channel.send(message.author.top_role.permissions.manage_nicknames)
        elif perm == "roles":
            await message.channel.send(message.author.top_role.permissions.manage_roles)
        else:
            await message.channel.send("Not a proper permission title")
    if "!nick" in message.content.lower():
        newnick = message.content[6::]
        await message.author.edit(nick = newnick)
    if "!pingroulette" in message.content.lower():
        memlist = message.guild.members
        selecteduser = memlist[random.randint(0,len(memlist)-1)]
        await message.channel.send(selecteduser.mention)
    if "!channel" in message.content.lower():
        for i in message.guild.channels:
            print(i)
    if "!clone" in message.content.lower():
        channame = message.content[7::]
        currchan = message.channel
        await currchan.clone(name = channame)
    if message.content.lower() == "!delete":
        await message.channel.delete()
    if "!deletechan" in message.content.lower():
        channame = message.content[12::]
        channeltodelete = ""
        for i in message.guild.text_channels:
            if channame == i.name:
                channeltodelete = i
                await channeltodelete.delete()
                await message.channel.send("Channel has been deleted!")
                break
        else:
            await message.channel.send("No channel by that name!")
    if "!createchan" in message.content.lower():
        channame = message.content[11::]
        await message.guild.create_text_channel(channame)
    if message.content.lower() == "!nummessages":
        counter = 0
        async for i in message.channel.history():
            counter += 1
        await message.channel.send('There are ' + str(counter) + " messages in this channel")
    if message.content.lower() == "!numspecificmessages":
        counter = 0
        async for i in message.channel.history():
            if message.author == i.author:
                counter += 1
        await message.channel.send('There are ' + str(counter) + " messages in this channel by " + str(message.author))
    if message.content.lower() == "!createinvite":
        invite = await message.channel.create_invite(max_age = 120, max_uses = 1, unique = True)
        await message.channel.send(invite)
    if message.content.lower()[0:8] == "!echodm ":
        param = message.content[8::]
        if message.author.dm_channel == None:
            dmchan = await message.author.create_dm()
        else:
            dmchan = message.author.dm_channel
        await dmchan.send(param)
    if message.content.lower() == "!dminv":
        invite = await message.channel.create_invite(max_age = 120, max_uses = 1, unique = True)
        if message.author.dm_channel == None:
            dmchan = await message.author.create_dm()
        else:
            dmchan = message.author.dm_channel
        await dmchan.send(invite)
bot.run(os.environ['bot_key'])
