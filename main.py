import discord
import os
import requests
import json
import random
import csv


client = discord.Client()

# list of curse words created using csv
curse = []
curse_file = "censor/bad-words-en.csv"
with open(curse_file, 'r') as word:
    for i in csv.reader(word):
        curse.append(i)

curse_final = []

for i in curse:
    index = curse.index(i)
    curse_final.append(curse[index][0])

# messages if curse words are used in the server
anti_curse = [
    "Please mind your language.",
    "Don't use that language here in this server.",
    "You could face temporary ban if you keep on using that language!"
]

# fetch quotes from zenquotes.io


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    #quote = json_data[0]['h']
    return(quote)


@client.event
async def on_ready():
    print(
        "We have logged in as {0.user} /n Bot created by Tushar G. (github.com/tushgaurav)".format(client))


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

    if any(word in msg for word in curse_final):
        await message.channel.send(random.choice(anti_curse))


client.run('Nzk1Mjc1NzQyMTkxMjg4MzIx.X_HAQA.bYEYoDBVRMt__xiqedIKi3M7rLQ')
