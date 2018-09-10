import discord
from discord.ext import commands
import datetime

def is_owner_check(message):
    return message.author.id == '429118689367949322'

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    @is_owner()
    async def eval(self, ctx, *, code : str):
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await self.bot.say(python.format(result))


def setup(bot):
    bot.add_cog(Owner(bot))
