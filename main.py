import discord
import os
import requests
import json

client = discord.Client()

curse = ["sad", "happy", "pro", "noob", "coding"]

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

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  elif message.content.startswith('$gyan'):
    quote = get_quote()
    await message.channel.send(quote)


client.run(os.getenv('TOKEN'))
