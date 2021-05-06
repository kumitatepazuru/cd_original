import logging

from discord.ext import commands


class compile(commands.Cog):
    PRINT_TXT = ""

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    def p(self,*args, sep=' ', end='\n', file=None, flush: bool = False):
        self.PRINT_TXT = sep.join(*args) + end

    @commands.command(aliases=['cep'])
    async def compile_python(self, ctx, *args):
        exec('import os;os.system("echo danger!")', {'__builtins__': None,"print":self.p}, {})
        ctx.send("```python\n"+self.PRINT_TXT+"\n```")


def setup(bot):
    bot.add_cog(compile(bot))
