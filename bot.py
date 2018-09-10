import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import asyncio
import os
import io


prefix = "e!"
bot = discord.Client()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

minutes = 0
hour = 0
days = 0
use = 0

@bot.event
async def on_member_join(member):
    server = member.server
    if server.id == "418001869781205002":
        channel = bot.get_channel("486056709974917139")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel, msg)
    else:
        return
@bot.event
async def on_member_remove(member):
    server = member.server
    if server.id == "418001869781205002":
        channel = bot.get_channel("486056709974917139")
        server = member.server
        msg = "**:wave: {} Just Left Us , Hope You See Soon!**".format(member)
        await bot.send_message(channel, msg)

    else:
        return


@bot.event
async def on_command(command, ctx):
    global use
    use +=1

@bot.command(pass_context = True)
async def usages(ctx):
    embed=discord.Embed()
    embed.add_field(name="Usages.. :wrench:", value=f"**{use}** Commands Used After The Bot Restart!", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def ping(ctx):
    pingtime = time.time()
    embed=discord.Embed(description="**Pong !...**")
    pingms = await bot.send_message(ctx.message.channel, embed=embed)
    await asyncio.sleep(2)
    ping = (time.time() - pingtime) * 1000
    embed.add_field(name=":ping_pong:", value="It Took Me :-\n**%d Micro Seconds**" % ping , inline=True)
    await bot.edit_message(pingms,embed=embed)

@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="Scanner's Server".format(len(set(bot.get_all_members()))),type=3))


@bot.command(pass_context=True)
async def uptime(ctx):
    embed=discord.Embed()
    embed.add_field(name="EDGE Uptime.. :clock10:", value="Online For **|** **{0}** Days **{1}** Hour(s) and **{2}** Minute(s) !".format(days , hour , minutes), inline=True)
    await bot.send_message(ctx.message.channel , embed=embed)


async def tutorial_uptime():
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    global days
    days = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if hour == 24:
            minutes = 0
            hour = 0
            days +=1
bot.loop.create_task(tutorial_uptime())

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

        bot.run(os.getenv("TOKEN"))
