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

# GLOBAL VARIABLES - needed for conversions etc
global userTimezone

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
            await channel.send("Upon typing the command, the program will prompt you to enter your **GMT offset**.")
        break
    
# Test command to see if the ping by ID function works (it does!)
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! **{round(client.latency * 1000)}** ms")

# Set timezone command
@client.command()
async def settimezone(ctx):
    validTimezoneGiven = False
    
    await ctx.send("Please enter your GMT offset (example: GMT-14):\n*Please ensure that GMT is capitalized. If you would like to stop using this command, type 'exit'.*")
    while validTimezoneGiven == False:
        global userTimezone
        msg = await client.wait_for('message')

        elementToLookFor = "Etc/" + msg.content

        if elementToLookFor in pytz.all_timezones:
            # Makes searching through the pytz array easier so we don't have to conactenate 2 strings all the time
            userTimezone = elementToLookFor
            await msg.channel.send("Your timezone has been set to **{}**".format(msg.content))
            break
        elif 'exit' in msg.content.lower():
            await msg.channel.send("Exiting command...")
            await msg.channel.send("Now ready for other input.")
            break
        else:
            await msg.channel.send("Invalid input. Please try again:\n*Please ensure that GMT is capitalized. If you would like to stop using this command, type 'exit'*.")


client.run('')