import discord
from discord.ext import commands
import time
import datetime
import os
import io

class Other():
    def __init__(self, bot):
        self.bot = bot
    async def on_command_error(self, error: Exception, ctx: commands.Context):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed()
            embed.add_field(name="Failure", value="Invalid Bad Argument!  :face_plam:", inline=False)
            await self.bot.send_message(ctx.message.channel,embed=embed)


        elif isinstance(error, commands.CheckFailure):
            if ctx.command.name == 'config':
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Adminstrator` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "ban":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Ban Members` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "kick":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Kick Members` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "mute":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Manage Channels` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == 'config welcome_enable':
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Adminstrator` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "addrole":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Manage Roles` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "removerole":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Manage Roles` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
            elif ctx.command.name == "rename":
                embed=discord.Embed()
                embed.add_field(name="Missing Permissions", value="You Need `Manage Nicknames` to This!", inline=False)
                await self.bot.send_message(ctx.message.channel,embed=embed)
        else:
            embed=discord.Embed()
            embed.add_field(name="Error Occurred In Last Command", value="```py\n{}\n```".format(error), inline=False)
            embed.set_footer(text="If This Error Become Unstoppable Please Contact Us ! Methods Below")
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.send_message(ctx.message.author , embed=embed)
            await self.bot.send_message(ctx.message.author,"Support Server :- https://discord.gg/ZA4KpSy\nRequest Support :- `e!askhelp [Error]`")

        
    @commands.command(pass_context=True)
    async def invites (self ,ctx):
         x = await self.bot.invites_from(ctx.message.server)
         await self.bot.say(len(x))
    @commands.command(pass_context=True)
    async def shrug(self, ctx):
        """Shrugs!"""
        await self.bot.say('¯\_(ツ)_/¯')

    @commands.command(pass_context=True)
    async def tableflip(self, ctx):
        """Tableflip!"""
        await self.bot.say('(╯°□°）╯︵ ┻━┻')

    @commands.command(pass_context=True)
    async def unflip(self, ctx):
        """Unfips!"""
        await self.bot.say('┬─┬﻿ ノ( ゜-゜ノ)')

    @commands.command(pass_context=True)
    async def face(self, ctx):
        """Lenny Face!"""
        await self.bot.say('( ͡° ͜ʖ ͡°)')

    @commands.command(pass_context=True)
    async def membercount(self ,ctx):
        server = ctx.message.server
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        bots = 0
        for member in server.members:
            if member.bot:
                bots += 1

        embed=discord.Embed(title=ctx.message.server.name, url="https://discordapp.com/branding")
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name="Server Name", value=ctx.message.server.name, inline=False)
        embed.add_field(name="Total Members", value=len(ctx.message.server.members), inline=False)
        embed.add_field(name="Online Members", value=online, inline=False)
        embed.add_field(name="Bot Users", value=bots, inline=False)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def serverinfo(self , ctx):
        server = ctx.message.server
        text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.voice])

        embed=discord.Embed(title="Server Information", url="https://discordapp.com/branding")
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Server Owner", value=ctx.message.server.owner, inline=True)
        embed.add_field(name="Server Owner ID", value=ctx.message.server.owner.id, inline=True)
        embed.add_field(name="Server Roles", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Server Members", value=len(ctx.message.server.members), inline=True)
        embed.add_field(name="Server Reigon", value=ctx.message.server.region, inline=True)
        embed.add_field(name="Text Channels", value=text_channels, inline=True)
        embed.add_field(name="Voice Channels", value=voice_channels, inline=True)
        embed.set_footer(text="Server Info Requested By {} | {} ".format(ctx.message.author.name , ctx.message.server.name),icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def test(self , ctx):
        await self.bot.say("<a:loading:438292576588791809> RAM {} MB\n CPU {}%".format(self.process.memory_full_info().uss / 1024**2,
        self.process.cpu_percent() / psutil.cpu_count()))

    @commands.command(pass_context=True)
    async def afk (self , ctx , *args):
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
            await self.bot.say(embed=embed)
            await self.bot.delete_message(ctx.message)
            await self.bot.wait_for_message(author=ctx.message.author)
            embed=discord.Embed()
            embed.add_field(name="{} is Now Back! :wave:".format(ctx.message.author.name), value="**{}**, Welcome Back !".format(ctx.message.author.name,name), inline=False)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def userinfo(self , ctx , user:discord.Member=None):
        if user is None:
            author = ctx.message.author
            embed=discord.Embed(title="{}'s Information".format(author.name), url=author.avatar_url)
            embed.set_author(name=author.name, icon_url=author.avatar_url)
            embed.set_thumbnail(url=author.avatar_url)
            embed.add_field(name="Name", value=author, inline=True)
            embed.add_field(name="Discriminator", value=author.discriminator, inline=True)
            embed.add_field(name="ID", value=author.id, inline=True)
            embed.add_field(name="Status", value=author.status, inline=True)
            embed.add_field(name="Playing", value=author.game, inline=True)
            embed.add_field(name="Top Role", value=author.top_role, inline=True)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.say(embed=embed)
        else:
            author = user
            embed=discord.Embed(title="{}'s Information".format(author.name), url=author.avatar_url)
            embed.set_author(name=author.name, icon_url=author.avatar_url)
            embed.set_thumbnail(url=author.avatar_url)
            embed.add_field(name="Name", value=author, inline=True)
            embed.add_field(name="Discriminator", value=author.discriminator, inline=True)
            embed.add_field(name="ID", value=author.id, inline=True)
            embed.add_field(name="Status", value=author.status, inline=True)
            embed.add_field(name="Playing", value=author.game, inline=True)
            embed.add_field(name="Top Role", value=author.top_role, inline=True)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self , ctx , user:discord.Member=None):
        if user is None:
            if ctx.message.author.avatar_url:
                avatar = ctx.message.author.avatar_url
            else:
                avatar = ctx.message.author.default_avatar_url

            embed=discord.Embed(title="Your Avatar URL", url=avatar)
            embed.set_author(name=ctx.message.author, icon_url=avatar)
            embed.set_image(url=avatar)
            await self.bot.say(embed=embed)
        else:
            if user.avatar_url:
                avatar = user.avatar_url
            else:
                avatar = user.default_avatar_url

            embed=discord.Embed(title="{}'s Avatar URL".format(user.name), url=avatar)
            embed.set_author(name=user, icon_url=avatar)
            embed.set_image(url=avatar)
            await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def suggest(self , ctx , *args):
        Sargs = ' '.join(args)
        if ctx.message.server.id == "418001869781205002":
            if Sargs == "":
                embed=discord.Embed()
                embed.add_field(name="Suggestion Empty", value="Your Suggestion Cannot Be Empty", inline=False)
                await self.bot.say(embed=embed)

            channel = self.bot.get_channel("439368852057620480")

            embed=discord.Embed()
            embed.add_field(name=f"New Suggestion!, value=\n\n**User:** {ctx.message.author}\n\n**Suggestion:** {Sargs}", inline=False)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.send_message(channel,embed=embed)

            embed=discord.Embed()
            embed.add_field(name="Suggestion Sent", value="Your Suggestion has Been Sent !", inline=False)
            embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await self.bot.send_message(ctx.message.author , embed=embed)

        else:
            return

def setup(bot):
    bot.add_cog(Other(bot))
