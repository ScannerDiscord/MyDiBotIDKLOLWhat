from fortnite_python import Fortnite
from fortnite_python.domain import Mode, Platform
import discord
from discord.ext import commands
import aiohttp
import datetime
import random

class FortRatings():
    def __init__(self, bot):
        self.bot = bot
        self.fortnite = Fortnite('274e0176-875b-400a-a7b4-fa2567990fda')
        
    @commands.command(pass_context=True)
    async def fdrop(self,ctx):
        choice = random.choice(['Anarchy Acres','Dsuty Divot','Fatal Fields','Flush Factory','Greasy Grove','Haunted Hills','Junk Junktion','Lonely Lodge',
                                'Loot Lake','Lucky Landing','Moisty Mire','Pleasant Park','Retail Row','Risky Reels','Salty Springs','Shifty Shafts','Snobby Shores',
                                'Tilted Towers','Tomato Town','Wailing Woods'])
        embed=discord.Embed()
        embed.add_field(name="Fortnite Location" , value="<:fortnite:484284936539471884> | You Should Drop At : **{}**".format(choice), inline=False)
        await self.bot.say(embed=embed)


    @commands.group(aliases=['fortnite'] , pass_context=True)
    async def fn (self, ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed()
            embed.add_field(name="Mode Needed", value="Mode Type Required `e!fn [solo , duo , squad] [player name]`", inline=False)
            await self.bot.say(embed=embed)

    @fn.command(pass_context=True)
    async def solo(self, ctx, player: str=None):
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname Required" , value="Player Name is Empty Use `e!fn [mode] [player]`", inline=False)
            await self.bot.say(embed=embed)
        try:
            player = self.fortnite.player(player)
        except:
            embed=discord.Embed()
            embed.add_field(name="Player Not Correct", value="I Think the Player You Entered is Not Correct", inline=False)
            await self.bot.say(embed=embed)
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Error", value="Could not find that player", inline=False)
            await self.bot.say(embed=embed)
        await self.bot.send_typing(ctx.message.channel)
        stats = player.getStats(Mode.SOLO)
        embed=discord.Embed(title="Fortnite Ratings", url="https://discord.gg/XjFdmH")
        embed.set_author(name=player.username)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/484283740131033098/index.png")
        embed.add_field(name="Name", value=player.username, inline=True)
        embed.add_field(name="Kills", value=stats.kills, inline=True)
        embed.add_field(name="Wins", value=stats.wins, inline=True)
        embed.add_field(name="K/D", value=stats.kd, inline=True)
        embed.add_field(name="Score", value=stats.score, inline=True)
        embed.add_field(name="Win Ratio", value=stats.winratio, inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)


    @fn.command(pass_context=True)
    async def duo(self, ctx, player: str=None):
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname Required" , value="Player Name is Empty Use `e!fn [mode] [player]`", inline=False)
            await self.bot.say(embed=embed)
        try:
            player = self.fortnite.player(player)
        except:
            embed=discord.Embed()
            embed.add_field(name="Player Not Correct", value="I Think the Player You Entered is Not Correct", inline=False)
            await self.bot.say(embed=embed)
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Error", value="Could not find that player", inline=False)
            await self.bot.say(embed=embed)
        await self.bot.send_typing(ctx.message.channel)
        stats = player.getStats(Mode.DUO)
        embed=discord.Embed(title="Fortnite Ratings", url="https://discord.gg/XjFdmH")
        embed.set_author(name=player.username)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/484283740131033098/index.png")
        embed.add_field(name="Name", value=player.username, inline=True)
        embed.add_field(name="Kills", value=stats.kills, inline=True)
        embed.add_field(name="Wins", value=stats.wins, inline=True)
        embed.add_field(name="K/D", value=stats.kd, inline=True)
        embed.add_field(name="Score", value=stats.score, inline=True)
        embed.add_field(name="Win Ratio", value=stats.winratio, inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)


    @fn.command(aliases=['sq'] , pass_context=True)
    async def squad(self, ctx, player: str=None):
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname Required" , value="Player Name is Empty Use `e!fn [mode] [player]`", inline=False)
            await self.bot.say(embed=embed)
        try:
            player = self.fortnite.player(player)
        except:
            embed=discord.Embed()
            embed.add_field(name="Player Not Correct", value="I Think the Player You Entered is Not Correct", inline=False)
            await self.bot.say(embed=embed)
        if player is None:
            embed=discord.Embed()
            embed.add_field(name="Error", value="Could not find that player", inline=False)
            await self.bot.say(embed=embed)
        stats = player.getStats(Mode.SQUAD)
        await self.bot.send_typing(ctx.message.channel)
        embed=discord.Embed(title="Fortnite Ratings", url="https://discord.gg/XjFdmH")
        embed.set_author(name=player.username)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/484283740131033098/index.png")
        embed.add_field(name="Name", value=player.username, inline=True)
        embed.add_field(name="Kills", value=stats.kills, inline=True)
        embed.add_field(name="Wins", value=stats.wins, inline=True)
        embed.add_field(name="K/D", value=stats.kd, inline=True)
        embed.add_field(name="Score", value=stats.score, inline=True)
        embed.add_field(name="Win Ratio", value=stats.winratio, inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)



def setup(bot):
    bot.add_cog(FortRatings(bot))
