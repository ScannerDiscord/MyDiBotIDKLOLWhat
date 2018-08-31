import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import os

minutes = 0
hour = 0
bot = discord.Client()
bot_prefix= "e!"
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

print("Logging...")
@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="e!help | {} Users".format(len(set(bot.get_all_members()))) , type=2))

   
@bot.command(pass_context=True)
async def wlc (ctx , user: discord.Member):
    await bot.send_message(user , "**Hello Welcome to Scanner's Server <:Pass:461924196390404106>**\n\nWe Are Trying to Bulid Up New Tanki Society to Play and Have Fun Thanks For Understanding the Value of If You Need Any Just Contact Scanner#4797  He Will Help You , Thank You ! (https://cdn.discordapp.com/attachments/376342591228084226/480637131979751424/sFFZsapvCHQ.png)")
    await bot.delete_message(ctx.message)
                  
@bot.command(pass_context=True)
async def refresh(ctx):
    await bot.change_presence(game=discord.Game(name="e!help | {} Users".format(len(set(bot.get_all_members()))) , type=2))

                           
@bot.event
async def on_member_join(member):
    server = member.server
    if server.id == "418001869781205002":
        if member.avatar_url:
            memberavatar = member.avatar_url
        else:
            memberavatar = member.default_avatar_url
        
        channel = bot.get_channel("418001869781205004")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        
        embed=discord.Embed(title="New User ", description="\n\n{}\n\n".format(msg))
        embed.set_author(name="Welcome!", icon_url=memberavatar)
        embed.set_footer(text=server.name , icon_url=server.icon_url)
        await bot.send_message(channel, embed=embed)
        
@bot.command(pass_context=True)
async def uptime(ctx):
    embed=discord.Embed()
    embed.add_field(name="Uptime", value=":clock10: **|** **{0}** Hour(s) and **{1}** Minute(s) !".format(hour , minutes), inline=True)
    await bot.send_message(ctx.message.channel , embed=embed)




@bot.command(pass_context=True)
async def report(ctx, *args ):
    args = ' '.join(args)
    if ctx.message.server.id == "418001869781205002":
        if ctx.message.author.avatar_url:
            avatar = ctx.message.author.avatar_url
        else:
            avatar = ctx.message.author.default.avatar_url
        
        channel = bot.get_channel("419143404631621652")
        await bot.send_message(ctx.message.author, "<:Pass:461924196390404106> | Your Report Was Sent to the Staff ! , Thanks For Reporting ")
        
        embed=discord.Embed(title="Information")
        embed.set_author(name="New Case ! ", icon_url=ctx.message.server.icon_url)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User" , value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Reason", value=args, inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await bot.send_message(channel,embed=embed)
        await bot.delete_message(ctx.message)
    else:
        return

@bot.command(pass_context=True)
async def suggest(ctx, *args ):
    Sargs = ' '.join(args)
    if ctx.message.server.id == "418001869781205002":
        if ctx.message.author.avatar_url:
            avatar = ctx.message.author.avatar_url
        else:
            avatar = ctx.message.author.default.avatar_url
        
        channel = bot.get_channel("439368852057620480")
        await bot.send_message(ctx.message.author, "<:Pass:461924196390404106> | Your Sugesstion Was Sent to the Staff ! , Thanks For the Suggestion !")
        
        embed=discord.Embed(title="Information")
        embed.set_author(name="New Suggestion ! ", icon_url=ctx.message.server.icon_url)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User" , value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Suggestion", value=Sargs, inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await bot.send_message(channel,embed=embed)
        await bot.delete_message(ctx.message)

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
bot.run(os.getenv("TOKEN"))
