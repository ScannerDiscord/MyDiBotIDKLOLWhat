import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime

minutes = 0
hour = 0
bot = discord.Client()
bot_prefix= "!"
bot = commands.Bot(command_prefix=bot_prefix)

print("Logging...")
@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="Professionals" , type=3))
    

@bot.event
async def on_member_join(member):
    server = member.server
    if server.id == "480248440148852757":
        if member.avatar_url:
            memberavatar = member.avatar_url
        else:
            memberavatar = member.default.avatar_url
        
        channel = bot.get_channel("480248440677203969")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        
        embed=discord.Embed(title="New User ", description="\n\n{}\n\n".format(msg))
        embed.set_author(name="Welcome!", icon_url=memberavatar)
        embed.set_footer(text=server.name , icon_url=server.icon_url)
        await bot.send_message(channel, embed=embed)
        
@bot.command(pass_context=True)
async def uptime(ctx):
    embed=discord.Embed()
    embed.add_field(name="Uptime", value=":clock10: **|** Providing Profesional **{0}** Hour(s) and **{1}** Minute(s) !".format(hour , minutes), inline=True)
    await bot.send_message(ctx.message.channel , embed=embed)




@bot.command(pass_context=True)
async def report(ctx, *args ):
    args = ' '.join(args)
    if ctx.message.server.id == "480248440148852757":
        if ctx.message.author.avatar_url:
            avatar = ctx.message.author.avatar_url
        else:
            avatar = ctx.message.author.default.avatar_url
        
        channel = bot.get_channel("480263377201922058")
        await bot.send_message(ctx.message.author, "<:Pass:461924196390404106> | Your Report Was Sent to the Staff ! , Thanks For Reporting ")
        
        embed=discord.Embed(title="Information")
        embed.set_author(name="New Case ! ", icon_url=ctx.message.server.icon_url)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User" , value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Reason", value=args, inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await bot.send_message(channel,embed=embed)
    else:
        return

@bot.command(pass_context=True)
async def suggest(ctx, *args ):
    Sargs = ' '.join(args)
    if ctx.message.server.id == "480248440148852757":
        if ctx.message.author.avatar_url:
            avatar = ctx.message.author.avatar_url
        else:
            avatar = ctx.message.author.default.avatar_url
        
        channel = bot.get_channel("480263813770379264")
        await bot.send_message(ctx.message.author, "<:Pass:461924196390404106> | Your Sugesstion Was Sent to the Staff ! , Thanks For the Suggestion !")
        
        embed=discord.Embed(title="Information")
        embed.set_author(name="New Suggestion ! ", icon_url=ctx.message.server.icon_url)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User" , value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Suggestion", value=Sargs, inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await bot.send_message(channel,embed=embed)
    else:
        return





async def tutorial_uptime():
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
bot.loop.create_task(tutorial_uptime())
bot.run("NDgwMjYyNzgxMzI5OTk3ODI0.Dlp26g.k36enKs_tQ0LSXeXScC0oIiE1wo")
