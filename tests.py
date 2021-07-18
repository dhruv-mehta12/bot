from datetime import datetime
import discord
import time

datetime_ = datetime


async def message_ping(message):
    var1 = datetime_.now()
    await message.channel.send(message)
    var2 = datetime_.now()
    print((var2 - var1).seconds)
