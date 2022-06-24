from decouple import config
import discord

BOT_KEY = config("BOT_KEY")

client=discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")


client.run(BOT_KEY)
