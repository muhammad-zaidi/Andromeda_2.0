import discord
import random
from discord.ext import commands


class repeat(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(repeat(client))
