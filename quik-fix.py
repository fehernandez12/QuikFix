import discord
import time
import os
import sys
import json
from discord.ext import commands

token = ''
command_prefix = ''
users = dict()

def get_config():
    global token
    global command_prefix
    with open(os.path.join(sys.path[0], 'config/config.json')) as config_file:
        config_json = json.load(config_file)
        token = config_json.get('config').get('token')
        command_prefix = config_json.get('config').get('prefix')
        pass

def get_users():
    global users
    with open(os.path.join(sys.path[0], 'data/discord_member.json')) as users_file:
        users = json.load(users_file)

get_config()
get_users()
bot = commands.Bot(command_prefix)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)

@bot.command()
async def irony(ctx):
    await ctx.send('How many layers of irony are you on?')

@bot.command()
async def fiveorsix(ctx):
    await ctx.send('You are like a baby')
    time.sleep(2)
    await ctx.send('Watch this:')
    time.sleep(5)
    await ctx.send('**__*~~𝓢 𝓤 𝓒 𝓒~~*__**')

@bot.command()
async def register1(ctx, member):
    user = {
        member.user.id
    }
    users.update()
    await ctx.send('This command is on the making...')
    time.sleep(1)
    await ctx.send('You can tag <@244239956170637323> while we finish it, though.')



bot.run(token)