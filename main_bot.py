from decouple import config
from discord.ext import commands

BOT_KEY = config("BOT_KEY")
CMD_DEL = "del"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command(name=CMD_DEL)
async def delete(ctx,number_of_msg:int):
    messages=await ctx.channel.history(limit=number_of_msg+1).flatten()

    for each_msg in messages:
        await each_msg.delete()

bot.run(BOT_KEY)
