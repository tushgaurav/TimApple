import discord
import os
import requests
import json
import random
import csv
from decouple import config
#import sys

TOKEN = config('TOKEN')

client = discord.Client()

# list of curse words created using csv
load_words = []
curse_file = "censor/bad-words-en.csv"
with open(curse_file, 'r') as word:
    for i in csv.reader(word):
        load_words.append(i)

curse_en = []

for i in load_words:
    index = load_words.index(i)
    curse_en.append(load_words[index][0])

load_words.clear()

curse_file = "censor/bad-words-hindi.csv"
with open(curse_file, 'r') as word:
    for i in csv.reader(word):
        load_words.append(i)

curse_hi = []

for i in load_words:
    index = load_words.index(i)
    curse_hi.append(load_words[index][0])

# messages if curse words are used in the server
anti_curse_en = [
    "Please mind your language.",
    "Don't use that language here in this server!",
    "You could face temporary ban if you keep on using that language!",
    "Don't use foul language on this server!"
]

anti_curse_hi = [
    "मेरा मुंह मत खुलवाओ!",
    "में आजकल रंग बदलने में लोगों का मुकाबला नहीं कर पा रहा हूं!!",
    "तारीफों से भी जिंदा रह सकते हैं..",
    "सूखे हुए पत्तों की तरह मत बनाओ अपनी जिंदगी!"
]


################
# api
################

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    # quote = json_data[0]['h']
    return(quote)


def evil_insult():
    response = requests.get(
        'https://evilinsult.com/generate_insult.php?lang=en&type=json')
    json_data = json.loads(response.text)
    insult = json_data['insult']
    return(insult)

################
# main bot code
################


@client.event
async def on_ready():
    branding = """
╔╦╗┬┌┬┐  ╔═╗┌─┐┌─┐┬  ┌─┐
 ║ ││││  ╠═╣├─┘├─┘│  ├┤ 
 ╩ ┴┴ ┴  ╩ ╩┴  ┴  ┴─┘└─┘                               
               """
    print(branding)
    print("Logged in as {0.user}".format(client))
    print("Bot created by Tushar G. (github.com/tushgaurav)")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

# bot functions
    if msg.startswith('$hello'):
        await message.channel.send('Nameste!')

    if msg.startswith('$gyan'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$roast'):
        insult = evil_insult()
        await message.channel.send(insult)

# anti curse features
    if any(word in msg for word in curse_en):
        await message.channel.send(random.choice(anti_curse_en))
    elif any(word in msg for word in curse_hi):
        await message.channel.send(random.choice(anti_curse_hi))

client.run(TOKEN)
