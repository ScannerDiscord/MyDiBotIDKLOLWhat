import discord
from discord.ext import commands
import datetime

class HelpCog():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def help(self , ctx):
       if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="Help is Here !", url="https://discord.gg/QP6ZdwK", color=0xffffff)
        embed.set_author(name="EDGE Help", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name=":globe_with_meridians: General (9)", value="`e!help general`", inline=True)
        embed.add_field(name=":joy: Fun (10)", value="`e!help fun`", inline=True)
        embed.add_field(name="<:tankionline:483218839199285248> Tanki (3)", value="`e!help tanki`", inline=True)
        embed.add_field(name=":robot: Bot Related (3)", value="`e!help bot`", inline=True)
        embed.add_field(name="<:fortnite:484284936539471884> Fortnite (4)", value="`e!help fortnite`", inline=True)
        embed.add_field(name=":trophy: Moderation (8)", value="`e!help mod`", inline=True)
        embed.add_field(name="<:discord:484284728015323157> Invite Me", value="[Invite Link](https://discordapp.com/oauth2/authorize?client_id=480262781329997824&scope=bot&permissions=8)", inline=True)
        embed.add_field(name="<:discord:484284728015323157> Support Server", value="[Link](https://discord.gg/QP6ZdwK)", inline=True)
        embed.add_field(name="<:discord:484284728015323157> Owner", value="Scanner#4797", inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def general(self , ctx):
        embed=discord.Embed(title="Category General", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!avatar [user]", value="Get an Avatar of a User on the Server" , inline=False)
        embed.add_field(name="e!userinfo [user]", value="Get Some Information About a User" , inline=False)
        embed.add_field(name="e!serverinfo", value="Get Information on the Server", inline=False)
        embed.add_field(name="e!afk (message)", value="Set an AFK Status to Inform Your Firends", inline=False)
        embed.add_field(name="e!servericon", value="Get the Server Icon Of the Current Server", inline=False)
        embed.add_field(name="e!membercount", value="Check the Current members of the Server", inline=False)
        embed.add_field(name="e!shrug", value="Shrug !", inline=False)
        embed.add_field(name="e!tableflip", value="Table Flip!", inline=False)
        embed.add_field(name="e!unflip", value="Yea , Unflip!", inline=False)
        embed.add_field(name="e!face", value="Face :/", inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def fun (self ,ctx):
        embed=discord.Embed(title="Catergory Fun", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!roast [user]", value="Roast a User with this !", inline=False)
        embed.add_field(name="e!8ball", value="Ask a 8ball Question ", inline=False)
        embed.add_field(name="e!say", value="Say Something as the Bot!", inline=False)
        embed.add_field(name="e!rps rock", value="Play RPS With Bot Chossing Rock", inline=False)
        embed.add_field(name="e!rps paper", value="Play RPS With Bot Chossing Paper", inline=False)
        embed.add_field(name="e!rps scissor", value="Play RPS With Bot Chossing Scissor", inline=False)
        embed.add_field(name="e!troll [user]", value="i Know this is a bull shit command , just crap!", inline=False)
        embed.add_field(name="e!love [user]", value="Find Your True Love Using this!", inline=False)
        embed.add_field(name="e!pizza [user]", value="Find How many Pizzas You Eat Daily!", inline=False)
        embed.add_field(name="e!virus [user]", value="Send a Completly Fake Virus to Your Firend :d", inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)
    @help.command(pass_context=True)
    async def tanki(self , ctx):
        embed=discord.Embed(title="Category Tanki", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!ratings [user]", value="Show ratings of a Player!", inline=False)
        embed.add_field(name="e!container", value="Open a Container", inline=False)
        embed.add_field(name="e!exp [user]", value="Show How Experience Required to Rank Up ", inline=False)
        embed.add_field(name="e!dropgold", value="Drop a Gold Box", inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)
    @help.command(pass_context=True)
    async def bot (self ,ctx):
        embed=discord.Embed(title="Category Bot", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!ping", value="Check the Response time", inline=False)
        embed.add_field(name="e!botinfo", value="Get some Information Regarding the bot", inline=False)
        embed.add_field(name="e!invite", value="Get the Invite Link For EDGE", inline=True)
        embed.add_field(name="e!usages", value="Get How Many Commands Used after the Bot Restart", inline=True)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def fortnite(self,ctx):
        embed=discord.Embed(title="Category Fortnite", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!fn solo [player name]", value="Get Ratings of Solo Fortnite Player", inline=True)
        embed.add_field(name="e!fn duo [player name]", value="Get Ratings of Duo Fortnite Player", inline=True)
        embed.add_field(name="e!fn squad [player name]", value="Get Ratings of Squad Fortnite Player", inline=True)
        embed.add_field(name="e!fdrop", value="Not sure where to drop? Use Me" , inline=True)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def mod(self,ctx):
        embed=discord.Embed(title="Category Moderation", url="https://discord.gg/RzVTWnF")
        embed.set_author(name="EDGE Help", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="e!kick", value="Kicks a User", inline=False)
        embed.add_field(name="e!ban", value="Ban a User", inline=False)
        embed.add_field(name="e!prune [amount]", value="Delete some messages" , inline=False)
        embed.add_field(name="e!getbans", value="Get an Banned Users list!" , inline=False)
        embed.add_field(name="e!warn [user] [reason]", value="Warn a user!" , inline=True)
        embed.add_field(name="e!rename [user]", value="Change a nickname of someone!" , inline=False)
        embed.add_field(name="e!addrole [user] [name]", value="Add a role to a User!" , inline=False)
        embed.add_field(name="e!removerole [user] [name]", value="Remove a role to a User!" , inline=False)
        embed.set_footer(text=ctx.message.server.name,icon_url=ctx.message.server.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def askhelp (self , ctx , *args):
        args = ' '.join(args)
        channel = self.bot.get_channel("483162663786905600")
        msg = ctx.message.author

        embed=discord.Embed(title="Help Requested!", url="https://discord.gg/QP6ZdwK")
        embed.add_field(name="Name", value=msg, inline=True)
        embed.add_field(name="ID", value=msg.id, inline=True)
        embed.add_field(name="Server", value=ctx.message.server.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Help Requested", value=args, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.send_message(channel , embed=embed)

        embed=discord.Embed()
        embed.add_field(name="Help Sent!", value="Your Request Was Sent ! , Wait For the Respond !", inline=False)
        await self.bot.say(embed=embed)



def setup(bot):
    bot.add_cog(HelpCog(bot))
