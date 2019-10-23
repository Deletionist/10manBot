"""
file: myBot.py
author: Jordan Disciglio;
Date: 10/20/19
about: This script will be used as a Discord Bot. It will allow 10-12 man teams to be able to be randomly generated.
        It will have the ability to auto-assign captains if needed, and hopefully map bans in the future.

"""
import discord
import dbl
import random

from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    """
    Allows user to know the bot is ready
    :return: A string indicating the bot is connected and ready to function
    """
    print('Bot is Ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def creator(ctx):
    await ctx.send("Deletionist aka JD made this bot")


@client.command(brief="returns a list of the people in the voice channels in the server",)
async def tens(ctx, voice_channel_id):
    # A List that holds users in a voice channel
    memberList = []

    # First getting the voice channels
    voice_channel_list = ctx.guild.voice_channels

    # getting the members in the voice channel
    for voice_channels in voice_channel_list:
        # Find the correct voice channel in a server
        if int(voice_channels.id) == int(voice_channel_id):
            if len(voice_channels.members) != 0:
                # Add the users in the correct voice channel to the list
                for members in voice_channels.members:
                    memberList.append(members.name)
                # Check if the list has enough players
                if len(memberList) >= 10:
                    #pick a random Captain
                    a = random.randint(0, (len(memberList) - 1))
                    b = random.randint(0, (len(memberList) - 1))
                    #Prevent the same Captain
                    while a == b:
                        b = random.randint(0, (len(memberList) - 1))
                    captainA = memberList[a]
                    captainB = memberList[b]
                    await ctx.send("Team A Captain: " + str(captainA))
                    await ctx.send("Team B Captain: " + str(captainB))
                    await ctx.send("Incase you dont want Captains....")
                    await ctx.send("***********************")
                    random.shuffle(memberList)
                    random.shuffle(memberList)
                    print("Team A is: " + str(memberList[0:5]))
                    await ctx.send("Team A is: " + str(memberList[0:5]))
                    print("Team B is: " + str(memberList[5:10]))
                    await ctx.send("Team B is: " + str(memberList[5:10]))

                else:
                    await ctx.send("You need " + str((10 - (len(voice_channels.members))))
                                   + " more people in order to run 10's")
            else:
                await ctx.send("Please make sure that you're running this command in the correct server!")

client.run('NjM1MzY1NDc5NTIzMDI0OTA2.Xax5kg.BQT0T3YbMkPYEhaXcxdFebMq8as')

