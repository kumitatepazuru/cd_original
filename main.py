import logging

from discord.ext import commands


class compile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.command(aliases=['cep'])
    async def compile_python(self, ctx, args):
        PRINT_TXT = ""

        def p(*pr, sep=' ', end='\n', file=None, flush: bool = False):
            global PRINT_TXT
            PRINT_TXT += sep.join(*pr) + end

        exec(args, {'__builtins__': None, "print": p}, {})
        ctx.send("```python\n" + PRINT_TXT + "\n```")


def setup(bot):
    bot.add_cog(compile(bot))
