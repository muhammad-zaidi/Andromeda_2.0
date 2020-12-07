import discord
from discord.ext import commands
import os


def token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


client = commands.Bot(command_prefix='!')
token = token()
# await client.process_commands(message) AFTER client.event


@client.event
async def on_ready():
    print("Bot.py is ready")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
