import discord
from discord.ext import commands
import datetime

class Mod():
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def mute(self , ctx , user:discord.Member=None, *reason):
        overwrites = channel.overwrites_for(user)
        overwrites.send_messages = False
        overwrites.add_reactions = False
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Mute ! `e!mute [user] [reason]`", inline=True)
            await self.bot.say(embed=embed)
        if reason is None:
            reason = "-"
        else:
            for channel in ctx.message.server.channels:
                if channel.type != discord.ChannelType.text:
                    continue
                else:
                    if overwrites.send_messages is False in ctx.message.channel:
                        embed=discord.Embed()
                        embed.add_field(name="User Muted Here ?!", value="The Bot Notices the User Doest Have Permissions to Send Messages!", inline=True)
                        await self.bot.say(embed=embed)
                    else:
                        await self.bot.edit_channel_permissions(channel, user,
                                                                overwrites)
                        embed=discord.Embed()
                        embed.add_field(name="User Muted :ok_hand:", value=f"**User:** {user}\n**Admin/Moderator:** {ctx.message.author}\n**Reason:** {reason}", inline=True)
                        embed.timestamp = datetime.datetime.utcnow()
                        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def unmute(self,ctx,user:discord.Member=None):
        for channel in ctx.message.server.channels:
            if channel.type != discord.ChannelType.text:
                continue

        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Unmute ! `e!unmute [user]``", inline=True)
            await self.bot.say(embed=embed)
        else:
            if overwrites.send_messages is True in channel:
                embed=discord.Embed()
                embed.add_field(name="User is Not Muted Here ?!", value="The Bot Notices the User Has Permissions to Send Messages!", inline=True)
                await self.bot.say(embed=embed)
            else:
                await self.bot.delete_channel_permissions(channel, user)
                embed=discord.Embed()
                embed.add_field(name="User Unmuted :ok_hand:", value=f"**User:** {user}\n**Admin/Moderator:** {ctx.message.author}", inline=True)
                embed.timestamp = datetime.datetime.utcnow()
                await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def prune (self , ctx , amount:int=None):
        if amount is None:
            embed=discord.Embed()
            embed.add_field(name="Amount is Missing", value="Provide How Much Messages to Should Delete! `e!prune [amount]`", inline=True)
            await self.bot.say(embed=embed)
        else:
            deleted = await self.bot.purge_from(ctx.message.channel, limit=amount)
            embed=discord.Embed()
            embed.add_field(name="Deleted", value=f"**{len(deleted)}** Messages Deleted!\n**Admin/Moderator:** {ctx.message.author.name}", inline=True)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def getbans (self , ctx):
        x = await self.bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed=discord.Embed()
        embed.add_field(name="Check DM", value="I Sent You the List Via DM ,Check There!", inline=True)
        await self.bot.say(embed=embed)

        embed=discord.Embed()
        embed = discord.Embed(title = "List of Banned Members For {}".format(ctx.message.server.name), description = x)
        return await self.bot.send_message(ctx.message.author,embed = embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def warn(self , ctx , user:discord.Member=None, *reason):
        reason = ' '.join(reason)
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Warn ! `e!warn [user] [reason]`", inline=True)
            await self.bot.say(embed=embed)
        elif reason is None:
            embed=discord.Embed()
            embed.add_field(name="Reason?", value="We Need a Reason to Warn `e!warn [user] [reason]`", inline=True)
            await self.bot.say(embed=embed)
        else:
            await self.bot.delete_message(ctx.message)
            embed=discord.Embed()
            embed.add_field(name="Warned!", value=f"You Were Warned In {ctx.message.server.name} , {reason}", inline=True)
            await self.bot.send_message(user,embed=embed)

            embed=discord.Embed()
            embed.add_field(name="User Was Warned :warning:", value=f"{user} Was Warned In {ctx.message.server.name}\n**Admin/Moderator:** {ctx.message.author}", inline=True)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_nicknames=True)
    async def rename(self,ctx,user:discord.Member=None,nick:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Change Nickname ! `e!rename [user] [new nickname]`", inline=True)
            await self.bot.say(embed=embed)
        if nick is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname?", value="We Need a New Nickname to Rename `e!rename [user] [new nickname]`", inline=True)
            await self.bot.say(embed=embed)
        else:
            await self.bot.delete_message(ctx.message)
            await self.bot.change_nickname(user, nick)
            embed=discord.Embed()
            embed.add_field(name="User Was Rename! :ok_hand:", value=f"{user}'s Nickname Was Changed to {nick} In {ctx.message.server.name}\n**Admin/Moderator:** {ctx.message.author}", inline=True)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self,ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Add a role ! `e!addrole [user] [role]`", inline=True)
            await self.bot.say(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role?", value="We Need a Role Name or a Mention to Add `e!addrole [user] [role]`", inline=True)
            await self.bot.say(embed=embed)
        else:
            await self.bot.delete_message(ctx.message)
            newrole = discord.utils.get(ctx.message.server.roles, name=role)
            await self.bot.add_roles(user, newrole)
            embed=discord.Embed()
            embed.add_field(name="Role Added :ok_hand:" , value=f"Role @**{role}**  Was Added to {user}\n**Admin/Moderator:** {ctx.message.author}", inline=False)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self,ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Remove a role ! `e!removerole [user] [role]`", inline=True)
            await self.bot.say(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role?", value="We Need a Role Name or a Mention to Remove `e!removerole [user] [role]`", inline=True)
            await self.bot.say(embed=embed)
        else:
            newrole = discord.utils.get(ctx.message.server.roles, name=role)
            await self.bot.remove_roles(user, newrole)
            await self.bot.delete_message(ctx.message)
            embed=discord.Embed()
            embed.add_field(name="Role Removed :ok_hand:" , value=f"Role @**{role}**  Was Removed From {user}\n**Admin/Moderator:** {ctx.message.author}", inline=False)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(self , ctx , user:discord.Member , *reason):
            reason = ' '.join(reason)
            if user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Ban ! `e!ban [user]`", inline=False)
                await self.bot.say(embed=embed)
            elif user.id == bot.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Epic Troll", inline=True)
                await self.bot.say(embed=embed)
            elif user.id == ctx.message.server.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="No Epic Trolls , No Need to Ban Your Boss?", inline=True)
                await self.bot.say(embed=embed)
            else:
                await self.bot.kick(user)
                await self.bot.delete_message(ctx.message)
                embed=discord.Embed()
                embed.add_field(name="User Was Banned :hammer:", value=f"{user} Was Banned From {ctx.message.server.name}\n**Admin/Moderator:** {ctx.message.author}", inline=True)
                await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self , ctx , user:discord.Member , *reason):
            reason = ' '.join(reason)
            if user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Kick ! `e!kick [user]`", inline=False)
                await self.bot.say(embed=embed)
            elif user.id == "429118689367949322":
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Epic Troll", inline=True)
                await self.bot.say(embed=embed)
            elif user.id == ctx.message.server.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="What a Noob , No Need to Kick Your Boss?", inline=True)
                await self.bot.say(embed=embed)
            else:
                await self.bot.kick(user)
                await self.bot.delete_message(ctx.message)
                embed=discord.Embed()
                embed.add_field(name="Member Kicked :boot:", value=f"{user} Was Kicked From {ctx.message.server.name}\n**Admin/Moderator:** {ctx.message.author}", inline=True)
                await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Mod(bot))
