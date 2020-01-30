import discord
import time
import os
import sys
import json
from discord.ext import commands
import sqlite3

conn = sqlite3.connect(os.path.join(sys.path[0], 'QuikFix.db'))
db_cursor = conn.cursor()

bot = commands.Bot('.')

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

@bot.event
async def on_message(message):
    user_id = message.author.id
    lookup = db_cursor.execute('SELECT * FROM discord_user WHERE userid = %u' % user_id)
    if not db_cursor.fetchone():
        user_data = []
        user_data.append(message.author.discriminator)
        user_data.append(message.author.id)
        user_data.append(message.author.name)
        user_data.append(0)
        user_data.append(0)
        user_data.append(0)
        user_data.append(0)
        user_data.append(1000)
        arg = tuple(user_data)
        db_cursor.execute('INSERT INTO discord_user VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, NULL)', arg)
        conn.commit()
        result = db_cursor.fetchone()
        print("User {} has been added to the database.".format(message.author.name))
    else:
        return

@bot.command()
async def register1(ctx, message):
    user_id = message.author.id
    lookup = db_cursor.execute('SELECT plays_game FROM discord_user WHERE userid = %u' % user_id)
    if not db_cursor.fetchone():
        db_cursor.execute('UPDATE discord_user SET plays_game = 1 WHERE userid = %u' % user_id)
        conn.commit()
    else:
        pass

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def snowspam(ctx):
    count = 0
    await ctx.send('Starting mass pinging in 3...')
    time.sleep(1)
    await ctx.send('2...')
    time.sleep(1)
    await ctx.send('1...')
    while count < 200:
        count += 1
        remaining = str(200 - count)
        await ctx.send('<@244239956170637323> is gay\nRemaining pings: {}'.format(remaining))
    time.sleep(5)
    await ctx.send('Ok, just one more...')
    time.sleep(1)
    await ctx.send('Hi <@244239956170637323>')

bot.run('NjcxMTMzMjQzMjEwNDY1Mjkz.XjL-Jg.cMFzc_2Ayx05wu1UiAtY4aLYRFI')