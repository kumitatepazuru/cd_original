import logging

from discord.ext import commands


class compile(commands.Cog):
    PRINT_TXT = ""

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    def p(self, *pr, sep=' ', end='\n', file=None, flush: bool = False):
        self.logger.debug(str(pr))
        self.PRINT_TXT += sep.join(pr) + end

    @commands.command(aliases=['cep'])
    async def compile_python(self, ctx, args):
        self.PRINT_TXT = ""
        exec(args, {'__builtins__': None, "print": self.p}, {})
        await ctx.send("```python\n" + self.PRINT_TXT + "\n```")


def setup(bot):
    bot.add_cog(compile(bot))
