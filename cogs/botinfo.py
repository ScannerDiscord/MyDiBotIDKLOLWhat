import discord
from discord.ext import commands
import datetime

prefix = "e!"
bot = commands.Bot(command_prefix=prefix)
bot = discord.Client()

class BotInfo():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def botinfo(self , ctx):
        embed=discord.Embed(title="Bot Information")
        embed.set_author(name="EDGE", icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="Server Count", value=len(self.bot.servers), inline=True)
        embed.add_field(name="Member Count", value="{}".format(len(set(self.bot.get_all_members()))), inline=True)
        embed.add_field(name="Channel Count", value="{}".format(len([c for c in self.bot.get_all_channels()])), inline=True)
        embed.add_field(name="Bot Version", value="1.30", inline=True)
        embed.add_field(name="Bot Owner", value="Scanner#4797", inline=True)
        embed.add_field(name="Co-Owner", value="Sup#9999", inline=True)
        embed.add_field(name="Bot Language", value="Python", inline=True)
        embed.add_field(name="Discord Version", value="{}".format(discord.__version__), inline=True)
        embed.add_field(name="Memory Usage", value="0 MB-80 MB", inline=True)
        embed.add_field(name="Prefix", value="`e!`", inline=True)
        embed.add_field(name="Invite Link", value="[Click to Invite](https://discordapp.com/oauth2/authorize?client_id=480262781329997824&scope=bot&permissions=8)", inline=True)
        embed.add_field(name="Support Server", value="[Link to Support Server](https://discord.gg/k2gYcC2)", inline=True)
        embed.add_field(name="Thanks For Helping!", value="**Blload#6680** | **iWeeti#4990** | **MiMs#3590** | **Ahsan#3247**", inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="Made With Discord Python | Scanner#4797" , icon_url="https://cdn.discordapp.com/attachments/418008017712447500/482770360115134485/232720527448342530.png")
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def invite(self , ctx):
        embed=discord.Embed(title="Click That Link & I am In Your Server")
        embed.set_author(name="EDGE" , icon_url="https://cdn.discordapp.com/avatars/480262781329997824/03b3668e0f2ff2f5cb4a5715ea2c986e.jpg?size=2048")
        embed.add_field(name="Links" , value="[Click Here to Invite EDGE to Your Servers](https://discordapp.com/oauth2/authorize?client_id=480262781329997824&scope=bot&permissions=8)\n\n[Click Here to Join Support Server](https://discord.gg/k2gYcC2)", inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
