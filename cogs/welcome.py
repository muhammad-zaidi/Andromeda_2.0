import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("welcome.py is ready")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f"""Welcome to the server {member.mention}!""")
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f"""{member.mention} has left the server!""")



def setup(client):
    client.add_cog(Welcome(client))
