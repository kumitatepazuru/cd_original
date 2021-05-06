import logging

from discord.ext import commands


class compile(commands.Cog):
    PRINT_TXT = ""

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.command(aliases=['cep'])
    async def compile_python(self, ctx, args):
        def p(*print, sep=' ', end='\n', file=None, flush: bool = False):
            PRINT_TXT = sep.join(*print) + end
            ctx.send("```python\n" + PRINT_TXT + "\n```")
        exec(args, {'__builtins__': None, "print":p}, {})


def setup(bot):
    bot.add_cog(compile(bot))
