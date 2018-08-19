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
bot_prefix= "!"
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

print("Logging...")
@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="Professionals" , type=3))

@bot.command(pass_context=True)
async def battle(ctx , user : discord.Member = None):

    team = random.choice([ctx.message.author.display_name , user.display_name])
    team2 = random.choice([ctx.message.author.display_name , user.display_name])
    team3 = random.choice([ctx.message.author.display_name , user.display_name])
    chan = ctx.message.channel
    rturr = random.choice(["Firebird" , "Freeze" , "Smoky" , "Hammer" , "Striker" ,"Thunder" , "Railgun" , "Shaft" , "Magnum" , "Terminator" ,"Railgun XT" ,"Terminator XT" ])
    rhull = random.choice(["Titan" , "Viking" , "Hornet" , "Mammoth" , "Wasp" ,"Juggernaut"])
    mturr = random.choice(["Firebird" , "Freeze" , "Smoky" , "Hammer" , "Striker" ,"Thunder" , "Railgun" , "Shaft" , "Magnum" , "Terminator" ])
    scree = "https://cdn.discordapp.com/attachments/418001869781205004/480646580295172116/221587754554188_1084180384961583.png"
    mhull = random.choice(["Titan" , "Viking" , "Hornet" , "Mammoth" , "Wasp" ,"Juggernaut"])
    winner = random.choice([ctx.message.author.name , user.name])
    if user is None:
        await bot.say("<:Fail:461924435176325120> Mention a User to Start the Battle With ! ")
    if user.id == bot.user.id:
        await bot.say("Nope ! I Don't Want To Battle <:Fail:461924435176325120>")
    if user.id ==  ctx.message.author.id:
         await bot.say("<:Fail:461924435176325120>You Cannot Start the Battle Your Self")
    else:
        embed=discord.Embed(title="Battle Starts..", description="\n\n**Loading <:verified:419067353545048064>**\n\n")
        embed.set_author(name="{} VS {}".format(ctx.message.author.name , user.name), icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
        embed.set_thumbnail(url=scree)
        embed.add_field(name="Battle Details", value="**{}** - {} M3 , {} M3\n**{}** - {} M3 , {} M3".format(ctx.message.author.name
        ,rturr
        ,rhull
        ,user.display_name
        ,mturr
        ,mhull), inline=False)
        embed.set_footer(text="Battle Starts in Few Seconds")
        x = await bot.send_message(chan ,embed=embed)
        await asyncio.sleep(5)
        embed=discord.Embed(title="Battle Log ")
        embed.set_author(name="{} VS {}".format(ctx.message.author.display_name , user.display_name), icon_url="https://cdn.discordapp.com/attachments/433182340211146755/433485204925972480/Tanki-Online-Logo.png")
        embed.set_thumbnail(url=scree)
        embed.add_field(name="Log..", value="{} Spawn\n{} Spawn\n{} Shoot {}\n{} Go {} Behind and Shoot Him\n{} Used Repair Kit\nFinally {} Did  {} Kills and Won !".format(team
        ,ctx.message.author.display_name
        ,user.display_name
        ,team
        ,team3
        ,team
        ,team2
        ,winner
        ,random.randint(1,100)), inline=False)
        embed.add_field(name="Winner", value=winner, inline=False)
        embed.add_field(name="Rewards", value="{} - **{}** Crystals\n{} - **{}** Crystals".format(ctx.message.author.display_name
        ,random.randint(1 , 100)
        ,user.display_name
        ,random.randint(2, 100)), inline=True)
        embed.add_field(name="Turrents and Hulls" , value="**{}** - {} M3 , {} M3\n**{}** - {} M3  , {} M3".format(ctx.message.author.display_name,
        rturr,
        rhull,
        user.display_name,
        mturr,
        mhull), inline=True)
        embed.set_footer(text="{} Won | Challenger {}".format(winner , ctx.message.author.display_name) , icon_url="https://cdn.discordapp.com/attachments/433182340211146755/433485204925972480/Tanki-Online-Logo.png")
        x = await bot.edit_message(x ,embed=embed)

    
@bot.command(pass_context=True)
async def wlc (ctx , user: discord.Member):
    await bot.send_message(user , "**Hello Welcome to Scanner's Server <:Pass:461924196390404106>**\n\nWe Are Trying to Bulid Up New Tanki Society to Play and Have Fun Thanks For Understanding the Value of If You Need Any Just Contact Scanner#4797  He Will Help You , Thank You ! (https://cdn.discordapp.com/attachments/376342591228084226/480637131979751424/sFFZsapvCHQ.png)")
    await bot.delete_message(ctx.message)
                           
@bot.command(pass_context=True)
async def help (ctx):
    embed=discord.Embed(title="I Know I am Helping You ")
    embed.set_author(name="EDGE Help ", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
    embed.add_field(name="!suggest", value="Suggest a Idea You Have", inline=False)
    embed.add_field(name="!report", value="Report Kids That are Violating Rules", inline=True)
    embed.add_field(name="!battle", value="Start a Battle With Your Firend !" , inline=False)    
    embed.add_field(name="!uptime", value="Check My Uptime" , inline=False)    
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
                           
                           
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
