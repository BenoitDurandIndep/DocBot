from decouple import config
import discord

BOT_KEY = config("BOT_KEY")
ID_CHANNEL=config("DI_CHANNEL")
MSG_IN, MSG_OUT,CMD_DEL = "ping", "pong","!del"

default_intents =discord.Intents.default()
default_intents.members=True
client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("Pong")

    if message.content.startswith(CMD_DEL):
        num=int(message.content.split()[1])
        messages = await message.channel.history(limit=num+1).flatten()

        for each_msg in messages:
            await each_msg.delete()


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel=client.get_channel(ID_CHANNEL)
    await general_channel.send(content=f"Welcome on this server {member.display_name}.")

client.run(BOT_KEY)
