import logging

from discord.ext import commands


async def p(ctx, *pr, sep=' ', end='\n', file=None, flush: bool = False):
    PRINT_TXT = sep.join(*pr) + end
    await ctx.send("```python\n" + PRINT_TXT + "\n```")


class compile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.command(aliases=['cep'])
    async def compile_python(self, ctx, args):
        exec(args, {'__builtins__': None, "print": lambda *ar, **kwargs: await p(ctx, ar, kwargs)}, {})


def setup(bot):
    bot.add_cog(compile(bot))
