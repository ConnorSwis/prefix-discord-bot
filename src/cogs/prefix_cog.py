from prefixes import Prefixes
from discord.ext import commands


class Prefixes_Cog(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.p = Prefixes()
        
    @commands.command()
    async def prefix(self, ctx: commands.Context, prefix=None):
        if prefix:
            self.p.set_prefix(ctx.author.id, prefix)
        prefix = self.p.get_prefix(ctx.author.id)[1]
        await ctx.reply(f"Your prefix is `{prefix}`")
            


def setup(client: commands.Bot):
    client.add_cog(Prefixes_Cog(client))