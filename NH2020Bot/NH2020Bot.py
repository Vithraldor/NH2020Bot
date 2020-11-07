'''
NewHacks Timezone Converter Bot

Made by Star, Maple, and Vith

'''

import discord
from discord.ext import commands, tasks
import asyncio
import datetime

client = commands.Bot(command_prefix = 'tz!')

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
    startMessage = "with time"
    await client.change_presence(activity = discord.Streaming(name = startMessage, url = "https://github.com/Vithraldor"))
    
# Test command to see if the ping by ID function works (it does!)
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! **{round(client.latency * 1000)}** ms")

@client.command()
async def testcmd(ctx):
    await ctx.send("This is a test message.")

client.run('')