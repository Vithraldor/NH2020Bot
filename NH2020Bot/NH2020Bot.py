'''
NewHacks Timezone Converter Bot

Made by Star, Maple, and Vith

'''

import discord
from pytz import timezone
import pytz

from discord.ext import commands, tasks
import asyncio
import datetime

client = commands.Bot(command_prefix = 'tz!')

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
    startMessage = "with time"
    await client.change_presence(activity = discord.Streaming(name = startMessage, url = "https://github.com/Vithraldor"))

# Message that the bot will send when it joins a server, prompting the user to enter their default timezone using tz!settimezone
@client.event()
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hi, I'm the **Timezone Conversion Reminder Bot**.\nTo get started, please set your timezone using **tz!settimezone**.")
        break
    
# Test command to see if the ping by ID function works (it does!)
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! **{round(client.latency * 1000)}** ms")

@client.command()
async def testcmd(ctx):
    await ctx.send("This is a test message.")

client.run('')