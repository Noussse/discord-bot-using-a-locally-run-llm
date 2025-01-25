import discord
import requests
import time
import asyncio
from discord.ext import commands
from collections import defaultdict
from dotenv import load_dotenv
import os
import CommunicationWithSage as Csage
import json

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')

with open('identities.json', 'r') as file:
    identities = json.load(file)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('pizza'):
        await message.channel.send("pizza")

    if message.content.lower().startswith('sage'):
        user_id = str(message.author.id)
        user_input = message.content[5:].strip()
        if user_id in identities:
            response = Csage.generate_response(identities[user_id], user_input)
        else:
            response = Csage.generate_response("You're talking with an unknown person. Try to find out who they are and be cautious.", user_input)

        await message.channel.send(response)


            
        


client.run(TOKEN)