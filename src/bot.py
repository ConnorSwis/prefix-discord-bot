import os
from pathlib import Path

import discord
import dotenv
from discord.ext import commands

from prefixes import Prefixes


os.chdir(Path(__file__).parent)
dotenv.load_dotenv('../.env')
TOKEN = os.getenv('TOKEN')
DEFAULT_PREFIX = os.getenv('DEFAULT_PREFIX')
prefixes = Prefixes(default=DEFAULT_PREFIX)


def prefix(client: commands.Bot, message: discord.Message):
    return prefixes.get_prefix(message.author.id)[1], DEFAULT_PREFIX

client = commands.Bot(prefix)

for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        client.load_extension("cogs."+cog[:-3])

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')


if __name__ == "__main__":
    client.run(TOKEN)
