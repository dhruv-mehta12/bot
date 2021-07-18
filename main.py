import re
import os
import datetime
from dotenv import load_dotenv
from discord import Client

load_dotenv()  # loading the env variables

client = Client()   # making a discord client

intents_greetings = ["hi", "hello", "hey"]
intents_sick = ["damn", "cool", "man"]


async def message_ping(message, reply):
    received_time = datetime.datetime.now()
    await message.channel.send(reply)
    reply_time = datetime.datetime.now()

    print(reply_time - received_time)  # ping = reply_time - received_time


@client.event
async def on_ready():
    print(f'{client.user} logged in')


@client.event
async def on_message(message):
    msg_list = re.findall(r"[\w']+", message.content)  # re.findall(r"[\w']+", data)

    if message.author == client.user:
        return

    for i in msg_list:
        if i in intents_greetings:
            await message_ping(message, "Hey!")


client.run(os.environ['TOKEN'])
