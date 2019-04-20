import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import asyncio
import os
import aiohttp
prefix = "s!"
bot = discord.Client()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

minutes = 0
hour = 0
days = 0
use = 0

@bot.command(pass_context = True)
async def help(ctx):
    embed=discord.Embed(title="Help!")
    embed.set_author(name="Help & Support", icon_url="https://cdn.discordapp.com/avatars/439579661245218816/dc56306745439b0babaa7e718daf477e.webp?size=1024")
    embed.add_field(name="s!avatar", value="Sends a Avatar Of a User `s!avatar [user]`", inline=False)
    embed.add_field(name="s!status", value="Check Scanner's Server Status", inline=False)
    embed.add_field(name="s!afk", value="Inform that Your AFK `e!afk [reason]`", inline=False)
    embed.add_field(name="s!prune", value="Delete Bulk Messages `e!prune [amount]`", inline=False)
    embed.add_field(name="s!warn", value="Warn a User `s!warn [reason]`", inline=False)
    embed.add_field(name="s!rename", value="Change the Nickname of a User `s!rename [user] [new nickname]`", inline=False)
    embed.add_field(name="s!addrole", value="Add a role to a User `s!addrole [user] [role]`", inline=False)
    embed.add_field(name="s!removerole", value="Remove a role from a user `s!removerole [user] [role]`", inline=False)
    embed.add_field(name="s!ban", value="Ban a User `s!ban [user] [reason]`", inline=False)
    embed.add_field(name="s!kick", value="Kick a User `s!kick [user] [reason]`", inline=False)
    embed.add_field(name="s!usages", value="Check How Many Command Uses Done After the Restart!", inline=False)
    embed.add_field(name="s!suggest", value="Suggest Something!  `e!suggest [idea]`", inline=False)
    embed.add_field(name="s!ping", value="Check the Bot is Alive?!?", inline=False)
    embed.add_field(name="s!uptime", value="Check the Uptime", inline=False)
    embed.add_field(name="s!ratings", value="Get Tanki Online Ratings `s!ratings [name]`", inline=False)
    embed.add_field(name="s!exp", value="Get How Much Expirence Required to rank up! `s!exp [name]`", inline=False)
    embed.add_field(name="s!container", value="Open a Container", inline=False)
    embed.add_field(name="s!say", value="Say Something `e!say [words]`", inline=False)
    embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await bot.send_message(ctx.message.author,embed=embed)
    await bot.add_reaction(ctx.message, "👍")


@bot.command(pass_context = True)
async def avatar(ctx , user:discord.Member=None):
        if user is None:
            if ctx.message.author.avatar_url:
                avatar = ctx.message.author.avatar_url
            else:
                avatar = ctx.message.author.default_avatar_url

            embed=discord.Embed(title="Your Avatar URL", url=avatar)
            embed.set_author(name=ctx.message.author, icon_url=avatar)
            embed.set_image(url=avatar)
            await bot.say(embed=embed)
        else:
            if user.avatar_url:
                avatar = user.avatar_url
            else:
                avatar = user.default_avatar_url

            embed=discord.Embed(title="{}'s Avatar URL".format(user.name), url=avatar)
            embed.set_author(name=user, icon_url=avatar)
            embed.set_image(url=avatar)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
async def status (ctx):
    server = ctx.message.server
    text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
    voice_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.voice])
    s = ctx.message.server
    bots = 0
    for member in s.members:
        if member.bot:
            bots +=  1
    embed=discord.Embed(title="Server Status")
    embed.set_author(name=s.name, icon_url=ctx.message.server.icon_url)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Members", value=len(s.members), inline=False)
    embed.add_field(name="Bots", value=bots, inline=False)
    embed.add_field(name="Text Channels", value=text_channels, inline=False)
    embed.add_field(name="Voice Channels", value=voice_channels, inline=False)
    embed.set_footer(text="Server Status Requested By {} | {} ".format(ctx.message.author.name , ctx.message.server.name),icon_url=ctx.message.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def afk (ctx , *args):
        name = ' '.join(args)
        if "@everyone" in name:
            embed=discord.Embed()
            embed.add_field(name="No Need!", value="No Need to Inform Everyone!", inline=False)
            await self.bot.say(embed=embed)
        elif "@here" in name:
            embed=discord.Embed()
            embed.add_field(name="No Need!", value="No Need to Inform Everyone!", inline=False)
            await self.bot.say(embed=embed)
        else:
            embed=discord.Embed()
            embed.add_field(name="{} is Now AFK! :wave:".format(ctx.message.author.name), value="**{}** is Now AFK: {}".format(ctx.message.author.name,name), inline=False)
            await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
            await bot.wait_for_message(author=ctx.message.author)
            embed=discord.Embed()
            embed.add_field(name="{} is Now Back! :wave:".format(ctx.message.author.name), value="**{}**, Welcome Back !".format(ctx.message.author.name,name), inline=False)
            await bot.say(embed=embed)


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
@commands.has_permissions(manage_messages=True)
async def prune ( ctx , amount:int=None):
        if amount is None:
            embed=discord.Embed()
            embed.add_field(name="Amount is Missing", value="Provide How Much Messages to Should Delete! `s!prune [amount]`", inline=True)
            await bot.say(embed=embed)
        else:
            deleted = await bot.purge_from(ctx.message.channel, limit=amount)
            embed=discord.Embed()
            embed.add_field(name="Deleted", value="**{}** Messages Deleted!\n**Admin/Moderator:** {}".format(len(deleted),ctx.message.author.name), inline=True)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def warn( ctx , user:discord.Member=None, *reason):
        reason = ' '.join(reason)
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Warn ! `s!warn [user] [reason]`", inline=True)
            await bot.say(embed=embed)
        elif reason is None:
            embed=discord.Embed()
            embed.add_field(name="Reason?", value="We Need a Reason to Warn `s!warn [user] [reason]`", inline=True)
            await bot.say(embed=embed)
        else:
            await bot.delete_message(ctx.message)
            embed=discord.Embed()
            await bot.send_message(user,embed=embed)

            embed=discord.Embed()
            embed.add_field(name="User Was Warned :warning:", value="{} Was Warned In {}\n**Admin/Moderator:** {}".format(user , ctx.message.server.name ,ctx.message.author), inline=True)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)
async def rename(ctx,user:discord.Member=None,nick:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Change Nickname ! `s!rename [user] [new nickname]`", inline=True)
            await bot.say(embed=embed)
        if nick is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname?", value="We Need a New Nickname to Rename `s!rename [user] [new nickname]`", inline=True)
            await bot.say(embed=embed)
        else:
            await bot.delete_message(ctx.message)
            await bot.change_nickname(user, nick)
            embed=discord.Embed()
            embed.add_field(name="User Was Rename! :ok_hand:", value="{}'s Nickname Was Changed to {} In {}\n**Admin/Moderator:** {}".format(user,nick,ctx.message.server.name
            ,ctx.message.author), inline=True)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Add a role ! `e!addrole [user] [role]`", inline=True)
            await bot.say(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role?", value="We Need a Role Name or a Mention to Add `e!addrole [user] [role]`", inline=True)
            await bot.say(embed=embed)
        else:
            await bot.delete_message(ctx.message)
            newrole = discord.utils.get(ctx.message.server.roles, name=role)
            await bot.add_roles(user, newrole)
            embed=discord.Embed()
            embed.add_field(name="Role Added :ok_hand:" , value="Role @**{}**  Was Added to {}\n**Admin/Moderator:** {}".format(role,user,ctx.message.author), inline=False)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Remove a role ! `s!removerole [user] [role]`", inline=True)
            await bot.say(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role?", value="We Need a Role Name or a Mention to Remove `s!removerole [user] [role]`", inline=True)
            await bot.say(embed=embed)
        else:
            newrole = discord.utils.get(ctx.message.server.roles, name=role)
            await bot.remove_roles(user, newrole)
            await bot.delete_message(ctx.message)
            embed=discord.Embed()
            embed.add_field(name="Role Removed :ok_hand:" , value="Role **@{}**  Was Removed From {}\n**Admin/Moderator:** {}".format(role,user,ctx.message.author), inline=False)
            await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def ban(ctx , user:discord.Member , *reason):
            reason = ' '.join(reason)
            if user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Ban ! `s!ban [user]`", inline=False)
                await bot.say(embed=embed)
            elif user.id == bot.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Epic Troll", inline=True)
                await bot.say(embed=embed)
            elif user.id == ctx.message.server.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="No Epic Trolls , No Need to Ban Your Boss?", inline=True)
                await bot.say(embed=embed)
            else:
                await bot.kick(user)
                await bot.delete_message(ctx.message)
                embed=discord.Embed()
                embed.add_field(name="User Was Banned :hammer:", value="{} Was Banned From {}\n**Admin/Moderator:** {}".format(user,ctx.message.server.name,ctx.message.author), inline=True)
                await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def kick(ctx , user:discord.Member , *reason):
            reason = ' '.join(reason)
            if user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Kick ! `s!kick [user]`", inline=False)
                await bot.say(embed=embed)
            elif user.id == "429118689367949322":
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Epic Troll", inline=True)
                await bot.say(embed=embed)
            elif user.id == ctx.message.server.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="What a Noob , No Need to Kick Your Boss?", inline=True)
                await bot.say(embed=embed)
            else:
                await bot.kick(user)
                await bot.delete_message(ctx.message)
                embed=discord.Embed()
                embed.add_field(name="Member Kicked :boot:", value="{} Was Kicked From {}\n**Admin/Moderator:** {}".format(user,ctx.message.server.name,ctx.message.author), inline=True)
                await bot.say(embed=embed)

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
    embed.add_field(name=":ping_pong:", value="Yes I am Still Alive\n**%d Micro Seconds**" % ping , inline=True)
    await bot.edit_message(pingms,embed=embed)

@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(activity=discord.Game(name="the AnimatedStick",type=3))

@bot.command(pass_context=True)
async def suggest(ctx , *args):
        Sargs = ' '.join(args)
        if ctx.message.server.id == "418001869781205002":
            channel = bot.get_channel("486055787437883412")
            await bot.delete_message(ctx.message)

            embed=discord.Embed()
            embed.add_field(name="New Suggestion!", value="\n\n**User:** {}\n\n**Suggestion:** {}".format(ctx.message.author,Sargs), inline=False)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await bot.send_message(channel,embed=embed)

            embed=discord.Embed()
            embed.add_field(name="Suggestion Sent", value="Your Suggestion has Been Sent !", inline=False)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await bot.send_message(ctx.message.author , embed=embed)
        else:
            return


@bot.command(pass_context=True)
async def uptime(ctx):
    embed=discord.Embed()
    embed.add_field(name="Uptime.. :clock10:", value="Online For **|** **{0}** Days **{1}** Hour(s) and **{2}** Minute(s) !".format(days , hour , minutes), inline=True)
    await bot.send_message(ctx.message.channel , embed=embed)

@bot.command(pass_context=True ,aliases=['xp'])
async def exp(ctx , user:str):
    url = "http://ratings.tankionline.com/get_stat/profile/?user={}&lang=en".format(user)
    async with aiohttp.get(url) as r:
      if r.status == 200:
        response = (await r.json())["response"]
        exp = response["score"]
        nextexp = response["scoreNext"]
        name = response["name"]

        if user is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname Required", value="Please Enter a Nickname `e!exp Scanner`", inline=True)
            await bot.say(embed=embed)

        if exp > 0:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879078966493195/big_1.png"
        if exp > 100:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879252652621824/big_2.png"
        if exp > 500:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879413642330112/big_3.png"
        if exp > 1500:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879626998448149/big_4.png"
        if exp > 3700:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879847518044190/big_5.png"
        if exp > 7100:
               thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883178219044864/big_6.png"
        if exp > 12300:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883279947563009/big_7.png"
        if exp > 20000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883347090243624/big_8.png"
        if exp > 29000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883424017973258/big_9.png"
        if exp > 41000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883518662311974/big_10.png"
        if exp > 57000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883595636310017/big_11.png"
        if exp > 76000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883736195694602/big_12.png"
        if exp > 98000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883803552153610/big_13.png"
        if exp > 125000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883928911511552/big_14.png"
        if exp > 156000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883976353153063/big_15.png"
        if exp > 192000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884062843764756/big_16.png"
        if exp > 233000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884115994116127/big_17.png"
        if exp > 280000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884221191585792/big_18.png"
        if exp > 332000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884285506912277/big_19.png"
        if exp > 390000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884357032509440/big_20.png"
        if exp > 450000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884406504194059/big_21.png"
        if exp > 527000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884467170738186/big_22.png"
        if exp > 606000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884523382669312/big_23.png"
        if exp > 692000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884602596425728/big_24.png"
        if exp > 787000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884667503149057/big_25.png"
        if exp > 889000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884729151029248/big_26.png"
        if exp > 1000000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884798138941441/big_27.png"
        if exp > 1122000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884854883811329/big_28.png"
        if exp > 1225000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884925784195082/big_29.png"
        if exp > 1400000:
                thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884995195863050/big_30.png"
        if exp > 1600000:
                thumb = "https://cdn.discordapp.com/attachments/418005628255207424/486047056092332042/big_31.png"

        await bot.send_typing(ctx.message.channel)
        embed=discord.Embed(title="Experience Need to Rank Up!", url="https://discord.gg/QP6ZdwK")
        embed.set_author(name=name)
        embed.set_thumbnail(url=thumb)
        embed.add_field(name="Nickname", value=name, inline=True)
        embed.add_field(name="Current Experience" , value="{:,}".format(exp), inline=False)
        embed.add_field(name="More Experience Needed", value="{:,}".format(nextexp - exp), inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def say(ctx , *name):
    name = ' '.join(name)
    if "@everyone" in name:
        embed=discord.Embed()
        embed.add_field(name="Stop Being A Kid", value="No Need Everyone!", inline=False)
        await bot.say(embed=embed)
    elif "@here" in name:
        embed=discord.Embed()
        embed.add_field(name="Stop Being A Kid", value="No Need Everyone!", inline=False)
        await bot.say(embed=embed)
    else:
        await bot.send_typing(ctx.message.channel)
        await bot.delete_message(ctx.message)
        await bot.say(name)

@bot.command(pass_context=True)
async def container(ctx):
    smoky=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Smoky XT** !\n\n")
    smoky.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483134853450170368/Smoky_XT.png")
    smoky.timestamp = datetime.datetime.utcnow()
    smoky.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    railgun=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Railgun XT** !\n\n")
    railgun.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483134979014918155/Railgun_XT_M3.png")
    railgun.timestamp = datetime.datetime.utcnow()
    railgun.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    h=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Hornet XT** !\n\n")
    h.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483135744324403200/Hornet_XT_M3.png")
    h.timestamp = datetime.datetime.utcnow()
    h.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    gold=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **5 Gold Boxes** !\n\n")
    gold.set_image(url="https://cdn.discordapp.com/attachments/418005628255207424/484385707779948557/2BAGUnn.png")
    gold.timestamp = datetime.datetime.utcnow()
    gold.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    armour=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Double Armors** !\n\n")
    armour.set_image(url="https://images-ext-2.discordapp.net/external/tJBHwCrvNRZ53T8ETS7zWBsW0e-IStFtI3N0K_8gX-g/https/i.imgur.com/HfrwpgC.png")
    armour.timestamp = datetime.datetime.utcnow()
    armour.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)


    damage=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Double Damage** !\n\n")
    damage.set_image(url="https://images-ext-1.discordapp.net/external/vHRbVQW3OmIl6cEhbwkxGOK4OhoSvmg1tZuuG7AnaKg/https/i.imgur.com/FWXPzIR.png")
    damage.timestamp = datetime.datetime.utcnow()
    damage.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    speed=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Speed Boosts** !\n\n")
    speed.set_image(url="https://images-ext-2.discordapp.net/external/6hXUSOXZxxf3HssVQpCktvf-fa3N83hkrm_Dx-KOTmo/https/i.imgur.com/prSNowH.png")
    speed.timestamp = datetime.datetime.utcnow()
    speed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    mines=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Mines** !\n\n")
    mines.set_image(url="https://images-ext-2.discordapp.net/external/_lMR1l16QJePjZ7XhBvF-FZIMKxekvvH_k9vjcov7a8/https/i.imgur.com/RAahEO7.png")
    mines.timestamp = datetime.datetime.utcnow()
    mines.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    all=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **100 Of All Supplies Pack** !\n\n")
    all.set_image(url="https://images-ext-2.discordapp.net/external/coqjnOiCxy39C4-nK5u0q-UWrKEzBzIHRn4Oy6S-60g/https/i.imgur.com/wTvTgWn.png")
    all.timestamp = datetime.datetime.utcnow()
    all.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    inf=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Inferno Paint** !\n\n")
    inf.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483139532170985472/Coloring_inferno.png")
    inf.timestamp = datetime.datetime.utcnow()
    inf.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    f=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Flora Paint** !\n\n")
    f.set_image(url="https://en.tankiwiki.com/images/en/9/94/Coloring_flora.png")
    f.timestamp = datetime.datetime.utcnow()
    f.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    c=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Corrosion Paint** !\n\n")
    c.set_image(url="https://en.tankiwiki.com/images/en/f/f2/Coloring_corrosion.png")
    c.timestamp = datetime.datetime.utcnow()
    c.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    l=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Lava Paint** !\n\n")
    l.set_image(url="https://en.tankiwiki.com/images/en/7/7e/Coloring_lava.png")
    l.timestamp = datetime.datetime.utcnow()
    l.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    e=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Eternity Paint** !\n\n")
    e.set_image(url="https://en.tankiwiki.com/images/en/a/af/Coloring_eternity.png")
    e.timestamp = datetime.datetime.utcnow()
    e.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    m=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Moonwalker Paint** !\n\n")
    m.set_image(url="https://en.tankiwiki.com/images/en/a/a8/Coloring_Moonwalker.png")
    m.timestamp = datetime.datetime.utcnow()
    m.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    g=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Ginga Paint** !\n\n")
    g.set_image(url="https://en.tankiwiki.com/images/en/5/54/Ginga_paint.png")
    g.timestamp = datetime.datetime.utcnow()
    g.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    gg=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Galaxy Paint** !\n\n")
    gg.set_image(url="https://en.tankiwiki.com/images/en/4/41/Galaxy_paint.png")
    gg.timestamp = datetime.datetime.utcnow()
    gg.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    p=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Prodigy 2.0 Paint** !\n\n")
    p.set_image(url="https://en.tankiwiki.com/images/en/c/c6/Paint_Prodigy2.png")
    p.timestamp = datetime.datetime.utcnow()
    p.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)

    x = random.choice([smoky , railgun , h , speed , damage , armour , gold ,inf , all , mines , f , c , l , e , g ,gg , m  ])
    await bot.say(embed=x)

@bot.command(pass_context=True)
async def ratings(ctx, user: str=None ):
    url = "http://ratings.tankionline.com/get_stat/profile/?user={}&lang=en".format(user)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            if r.status == 200:
                try:
                    response = (await r.json())["response"]
                    await bot.send_typing(ctx.message.channel)
                    kills = response["kills"]
                    deaths = response["deaths"]
                    crystals = response["earnedCrystals"]
                    gold = response["caughtGolds"]
                    exp = response["score"]
                    pre = response["hasPremium"]
                    name = response["name"]
                    gScore = response["gearScore"]

                    if user is None:
                        embed=discord.Embed()
                        embed.add_field(name="Nickname Required", value="Please Enter a Nickname `e!ratings Scanner`", inline=True)
                        await bot.say(embed=embed)

                    if exp > 0:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879078966493195/big_1.png"
                    if exp > 100:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879252652621824/big_2.png"
                    if exp > 500:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879413642330112/big_3.png"
                    if exp > 1500:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879626998448149/big_4.png"
                    if exp > 3700:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879847518044190/big_5.png"
                    if exp > 7100:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883178219044864/big_6.png"
                    if exp > 12300:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883279947563009/big_7.png"
                    if exp > 20000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883347090243624/big_8.png"
                    if exp > 29000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883424017973258/big_9.png"
                    if exp > 41000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883518662311974/big_10.png"
                    if exp > 57000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883595636310017/big_11.png"
                    if exp > 76000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883736195694602/big_12.png"
                    if exp > 98000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883803552153610/big_13.png"
                    if exp > 125000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883928911511552/big_14.png"
                    if exp > 156000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883976353153063/big_15.png"
                    if exp > 192000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884062843764756/big_16.png"
                    if exp > 233000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884115994116127/big_17.png"
                    if exp > 280000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884221191585792/big_18.png"
                    if exp > 332000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884285506912277/big_19.png"
                    if exp > 390000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884357032509440/big_20.png"
                    if exp > 450000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884406504194059/big_21.png"
                    if exp > 527000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884467170738186/big_22.png"
                    if exp > 606000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884523382669312/big_23.png"
                    if exp > 692000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884602596425728/big_24.png"
                    if exp > 787000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884667503149057/big_25.png"
                    if exp > 889000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884729151029248/big_26.png"
                    if exp > 1000000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884798138941441/big_27.png"
                    if exp > 1122000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884854883811329/big_28.png"
                    if exp > 1225000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884925784195082/big_29.png"
                    if exp > 1400000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884995195863050/big_30.png"
                    if exp > 1600000:
                        thumb = "https://cdn.discordapp.com/attachments/418005628255207424/486047056092332042/big_31.png"

                    embed=discord.Embed(title="Ratings For {}".format(name), url="http://ratings.tankionline.com/en/user/{}/".format(name), description="\n\n\n")
                    embed.set_author(name=name)
                    embed.set_thumbnail(url=thumb)
                    embed.add_field(name="Nickname", value=name, inline=True)
                    embed.add_field(name="Experience" , value="{:,}".format(exp), inline=True)
                    embed.add_field(name="Premium Status" , value=pre , inline=True)
                    embed.add_field(name="Kills", value="{:,}".format(kills), inline=True)
                    embed.add_field(name="Deaths", value="{:,}".format(deaths), inline=True)
                    embed.add_field(name="K/D", value="{0:.2f}".format(kills/deaths), inline=True)
                    embed.add_field(name="Gear Score", value="{:,}".format(gScore), inline=True)
                    embed.add_field(name="Crystals Obtained", value="{:,}".format(crystals), inline=True)
                    embed.add_field(name="Gold Boxes Caught", value="{:,}".format(gold), inline=True)
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
                    await bot.say(embed=embed)

                except:
                    embed=discord.Embed()
                    embed.add_field(name="Account Invalid", value="Account Does Not Exist !", inline=False)
                    await bot.say(embed=embed)


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
bot.run(os.getenv("TOKEN"))
