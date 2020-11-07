'''
NewHacks Timezone Converter Bot

Made by Catherine Li, Chaeyoung Lim, and Ashley Rivera for NewHacks 2020, a hackathon hosted by the University of Toronto's IEEE chapter.

'''
import discord
from discord.ext import commands, tasks

import pytz
from pytz import timezone

import asyncio

import datetime
from datetime import datetime, timedelta

client = commands.Bot(command_prefix = 'tz!')

# FOR TESTING PURPOSES - this prints out all the timezones as presented in pytz
print(pytz.all_timezones)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
    startMessage = "with time"
    await client.change_presence(activity = discord.Streaming(name = startMessage, url = "https://github.com/Vithraldor"))

# Message that the bot will send when it joins a server, prompting the user to enter their default timezone using tz!settimezone
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:

        # Loop the command until the bot finds a channel it can post its message in:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hi, I'm the **Timezone Conversion Reminder Bot**.\nTo get started, please set your timezone using **tz!settimezone**.")
        break
    
# Test command to see if the ping by ID function works (it does!)
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! **{round(client.latency * 1000)}** ms")

# Set timezone command
@client.command()
async def settimezone(ctx):
    await ctx.send

client.run('')