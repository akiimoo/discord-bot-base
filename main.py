import discord

cogs = [
    "cogs.ping"
]
PREFIX = "!"

class MyClient(discord.Client):
    async def on_ready(self):
        self.wait_until_ready()
        for cog in cogs:
            self.load_extension(cog)
        await print(f"Bot connected as {self.user}")

intents = discord.Intents.all()
client = MyClient(intents=intents)