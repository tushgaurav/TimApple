import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

curse = ["sad", "happy", "pro", "noob", "coding"]

anti_curse = [
  "Abe tu hai noob!",
  "Lega kya be?",
  "Nikal paheli fursat mei!"
]

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  #quote = json_data[0]['h']
  return(quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')
  elif msg.startswith('$gyan'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in curse):
    await message.channel.send(random.choice(anti_curse))


client.run(os.getenv('TOKEN'))
