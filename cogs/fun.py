import discord
from discord.ext import commands
import random
from random import choice, shuffle
import aiohttp
import functools
import asyncio
import datetime


class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def virus(self, ctx , user:discord.Member=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="Failure", value="Virus Seup was Failed Due to No Use Mentioned!", inline=True)
            await self.bot.say(embed=embed)
        if user.id == ctx.message.author.id:
            embed=discord.Embed()
            embed.add_field(name="Useless Life", value="Why You Hack Your Self ?", inline=True)
            await self.bot.say(embed=embed)
        if user.id == self.bot.user.id:
            embed=discord.Embed()
            embed.add_field(name="Wanna Hack Me?", value="Dude Go to Hell , this is not place for you !", inline=True)
            await self.bot.say(embed=embed)
        else:
            embed=discord.Embed(description="<a:loading:438292576588791809> **Packing Files.** ")
            x = await self.bot.say(embed=embed)
            await asyncio.sleep(1)
            embed=discord.Embed(description="<a:loading:438292576588791809> **Packing Files..** ")
            x = await self.bot.edit_message(x , embed=embed)
            await asyncio.sleep(1)
            embed=discord.Embed(description="<a:loading:438292576588791809> **Packing Files...** ")
            x = await self.bot.edit_message(x , embed=embed)
            await asyncio.sleep(2)
            embed=discord.Embed(description="<a:loading:438292576588791809> **Obtaining IP Adress** ")
            x = await self.bot.edit_message(x , embed=embed)
            await asyncio.sleep(2)
            embed=discord.Embed(description="<a:loading:438292576588791809> **Running** `Vrius-Setup.exe` ")
            x = await self.bot.edit_message(x , embed=embed)
            await asyncio.sleep(3)
            embed=discord.Embed(description="<a:loading:438292576588791809> **Finishing** ")
            x = await self.bot.edit_message(x , embed=embed)
            await asyncio.sleep(2)
            embed=discord.Embed(description=":<:Pass:461924196390404106> Sucessfull {}'s System is Full Of Virus Now\n\nGood Luck In the Future For Great Virus Attacks! **~EDGE**".format(user.name))
            x = await self.bot.edit_message(x , embed=embed)
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def pizza(self, ctx , user:discord.Member=None):
        if user is None:
            x = random.randint(2 , 50)
            embed=discord.Embed()
            embed.add_field(name="Pizza? :pizza:" , value="How Many Pizzas You Eat Daily : **{}** Pizzas".format(x), inline=False)
            await self.bot.say(embed=embed)
        else:
            y = random.randint(2 , 50)
            embed=discord.Embed()
            embed.add_field(name="Pizza? :pizza:" , value="How Many Pizzas {} Eat Daily : **{}** Pizzas".format(user.name , y), inline=False)
            await self.bot.say(embed=embed)



    @commands.command(pass_context=True)
    async def love(self, ctx, user: discord.Member):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name=":face_plam: Mention!", value="Mention a User , With Whom You Trying to Love?", inline=True)
            await self.bot.say(embed=embed)
        if user.id == self.bot.user.id:
            love = 100
            embed=discord.Embed()
            embed.add_field(name=":heart: Found Your True Love?", value="Love Bettween {} & {} Is **{}**%".format(user.name , ctx.message.author.name , love), inline=True)
            await self.bot.say(embed=embed)
        else:
            love = random.randint(1,100)
            embed=discord.Embed()
            embed.add_field(name=":heart: Found Your True Love?", value="Love Bettween {} & {} Is **{}**%".format(user.name , ctx.message.author.name , love), inline=True)
            await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def troll(self , ctx , user:discord.Member=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name=ctx.message.author.name , value="**{}** Was Banned From this Server".format(ctx.message.author.name) , inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/484380308314259456/314180188512583682.png")
            await self.bot.delete_message(ctx.message)
            await self.bot.say(embed=embed)
        else:
            embed=discord.Embed()
            embed.add_field(name=user.name , value="**{}** Was Banned From this Server".format(user.name) , inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/484380308314259456/314180188512583682.png")
            await self.bot.say(embed=embed)
            await self.bot.delete_message(ctx.message)

    @commands.group(pass_context=True)
    async def rps(self ,ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed()
            embed.add_field(name="Play As Rock", value="`e!rps rock` :black_circle:", inline=False)
            embed.add_field(name="Play As Paper", value="`e!rps paper` :newspaper:", inline=False)
            embed.add_field(name="Play As Scissor", value="`e!rps scissor` :scissors:", inline=True)
            await self.bot.say(embed=embed)
    @rps.command(pass_context=True)
    async def rock(self,ctx):
        await self.bot.say(random.choice([":scissors: **|** You Choose __Rock__ , I Choose __Scissors__ , **You Win**  :tada:",
                                                                  ":newspaper: **|** You Choose __Rock__ , I Choose __Paper__ , **You Lose**  :robot:",
                                                                  ":scissors: **|** You Choose __Rock__ , I Choose __Scissors__ , **You Win**  :tada:",
                                                                  ":newspaper: **|** You Choose __Rock__ , I Choose __Paper__ , **You Lose**  :robot:",
                                                                  ":black_circle:  **|** You Choose __Rock__ , I Choose __Rock__ , **Its Tie**  :confused:" ]))
    @rps.command(pass_context=True)
    async def paper(self,ctx):
        await self.bot.send_message(ctx.message.channel, random.choice([":scissors: **|** You Choose __Paper__ , I Choose __Scissors__ , **You Lose**  :robot:",
                                                                  ":newspaper: **|** You Choose __Paper__ , I Choose __Paper__ ,  **Its Tie**  :confused:",
                                                                  ":scissors: **|** You Choose __Paper__ , I Choose __Scissors___ , **You Lose**  :robot:",
                                                                  ":newspaper: **|** You Choose __Paper__ , I Choose __Paper___ ,  **Its Tie**  :confused:",
                                                                  ":black_circle:  **|** You Choose __Paper__ , I Choose __Rock__ , **You Win**  :tada:" ]))
    @rps.command(pass_context=True)
    async def scissor(self,ctx):
        await self.bot.send_message(ctx.message.channel, random.choice([":scissors: **|** You Choose __Scissors__ , I Choose __Scissors__ , **Its Tie**  :confused:",
                                                                  ":newspaper: **|** You Choose __Scissors__ , I Choose __Paper__ ,  **You Lose**  :robot:",
                                                                  ":scissors: **|** You Choose __Scissors__ , I Choose __Scissors__ ,  **Its Tie**  :confused",
                                                                  ":newspaper: **|** You Choose __Scissors__ , I Choose __Paper__ ,  **You Lose**   :robot:",
                                                                  ":black_circle:  **|** You Choose Scissors__ , I Choose __Rock__ , **You Lose**  :robot: " ]))
    @commands.command(pass_context=True)
    async def say(self , ctx , *name):
        name = ' '.join(name)
        if "@everyone" in name:
            embed=discord.Embed()
            embed.add_field(name="Stop Being A Kid", value="No Need Everyone!", inline=False)
            await self.bot.say(embed=embed)
        elif "@here" in name:
            embed=discord.Embed()
            embed.add_field(name="Stop Being A Kid", value="No Need Everyone!", inline=False)
            await self.bot.say(embed=embed)
        else:
            await self.bot.send_typing(ctx.message.channel)
            await self.bot.delete_message(ctx.message)
            await self.bot.say(name)

    async def on_message(self , message):
        if message.content.startswith("e!8ball "):
            await self.bot.send_message(message.channel,random.choice([":8ball: | **{},** It is Certain ".format(message.author.name),
                                                                      ":8ball: | **{},** It is Decidedly, So ?".format(message.author.name),
                                                                      ":8ball: | **{},** Without a doubt ".format(message.author.name),
                                                                      ":8ball: | **{},** Yes, definitely  ".format(message.author.name),
                                                                      ":8ball: | **{},** You may rely on it ".format(message.author.name),
                                                                      ":8ball: | **{},** As I see it, yes  ".format(message.author.name),
                                                                      ":8ball: | **{},** Most likely  ".format(message.author.name),
                                                                      ":8ball: | **{},** Outlook Looks Good  ".format(message.author.name),
                                                                      ":8ball: | **{},** Yes Bro ".format(message.author.name),
                                                                      ":8ball: | **{},** Signs point to yes ".format(message.author.name),
                                                                      ":8ball: | **{},** Reply lazy try again ".format(message.author.name),
                                                                      ":8ball: | **{},** Ask again later ".format(message.author.name),
                                                                      ":8ball: | **{},** Better not tell you now ".format(message.author.name),
                                                                      ":8ball: | **{},** Cannot predict now ".format(message.author.name),
                                                                      ":8ball: | **{},** Concentrate and ask again ".format(message.author.name),
                                                                      ":8ball: | **{},** Don't count on it  ".format(message.author.name),
                                                                      ":8ball: | **{},** My reply is no ".format(message.author.name),
                                                                      ":8ball: | **{},** My sources say no ".format(message.author.name),
                                                                      ":8ball: | **{},** Outlook is Not So Good  ".format(message.author.name),
                                                                      ":8ball: | **{},** Very doubtful  ".format(message.author.name)]))

    @commands.command(pass_context=True)
    async def roast (self , ctx ,name :discord.Member=None):
        if name is None:
            name = ctx.message.author

        await self.bot.delete_message(ctx.message)
        await self.bot.say(random.choice([":skull: **|** {} , You’re So Ugly That When You Cry, The Tears Roll Down The Back Of Your Head…Just To Avoid Your Face.".format(name),
                        ":fire: **|** {} , No Need For Insults, Your Face Says It All".format(name.mention),
                        ":fire: **|** {} , People Like You Are The Reason We Have Middle Fingers.".format(name.mention),
                        ":fire: **|** {} , Tell Me… Is Being Stupid A Profession Or Are You Just Gifted?".format(name.mention),
                        ":fire: **|** {} , Why Don’t You Slip Into Something More Comfortable. Like A Coma?".format(name.mention),
                        ":fire: **|** {} , When Your Mom Dropped You Off At The School, She Got A Ticket For Littering.".format(name.mention),
                        ":fire: **|** {} , Zombies Eat Brains. You’re Safe, Because You’re a Type Of It !".format(name.mention),
                        ":fire: **|** {} , What’s The Point Of Putting On Makeup, A Monkey Is Gonna Stay A Monkey.".format(name.mention),
                        ":fire: **|** {} , It’s Not That You Are Weird…It’s Just That Everyone Else Is Normal.".format(name.mention),
                        ":fire: **|** {} , It’s Not That I’m Smarter Than You, Its Just That You’re Dumber Than Everyone Else.".format(name.mention),
                        ":fire: **|** {} , Act Your Age Not Your Shoe Size.".format(name.mention),
                        ":fire: **|** {} , Scientists Are Trying To Figure Out How Long Human Can Live Without A Brain. You Can Tell Them Your Age.".format(name.mention),
                        ":fire: **|** {} , Stupidity Is Not A Crime So You Are Free To Go.".format(name.mention),
                        ":fire: **|** {} , Jealousy Is A Disease…Get Well Soon!".format(name.mention),
                        ":fire: **|** {} , Everyone Has The Right To Be Stupid, But You’re Abusing The Privilege.".format(name.mention),
                        ":fire: **|** {} , Just Keep Talking, I Yawn When I’m Interested.".format(name.mention),
                        ":fire: **|** {} , Your Are The Reason , God To Make A Middle Finger".format(name.mention),
                        ":fire: **|** {} , You’re So Much Smarter When You Don’t Speak!**".format(name.mention),
                        ":fire: **|** {} , You’re So Ugly, When You Were Born, The Doctor Said “Wheres The Baby?”".format(name.mention),
                        ":fire: **|** {} , You’re So Ugly, When You Were Born, Your Parents Sued The Doctor.".format(name.mention),
                        ":fire: **|** {} , You’re So Ugly, When You Were Born, Your Parents Asked For A Refund. ".format(name.mention),
                        ":fire: **|** {} , You’re So Ugly, When You Were Born, The Doctor Was The One Screaming Instead Of Your Mother.".format(name.mention),
                        ":fire: **|** {} , Where Were You When God Was Giving Out Common Sense?".format(name.mention),
                        ":fire: **|** {} , If I Hurt Your Feelings In Any Way I Just Want To Know From The Bottom Of My Heart That I Don’t Care.".format (name.mention),
                        ":fire: **|** {} , Your Are The Reason That HD Leave Tanki Online" .format(name.mention)]))


def setup(bot):
    bot.add_cog(Fun(bot))
