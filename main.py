import discord
import requests
import json
import random
import csv
from decouple import config
from keep_alive import keep_alive

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
    "Courage is fire, and bullying is smoke.",
    "Not all forms of abuse leave bruises.",
    "Don't use foul language on this server!",
    "I would rather be a little nobody than to be an evil somebody.",
    "If I were two-faced, would I be wearing this one?",
    "The average dog is a nicer person than you!",
    ""
]

anti_curse_hi = [
    "मेरा मुंह मत खुलवाओ!",
    "में आजकल रंग बदलने में लोगों का मुकाबला नहीं कर पा रहा हूं!!",
    "तारीफों से भी जिंदा रह सकते हैं..",
    "सूखे हुए पत्तों की तरह मत बनाओ अपनी जिंदगी!",
    "शरीफों की शराफत और हमारा,कमीनापन किसी को अच्छा, नहीं लगता!!"
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


def get_meme():
    response = requests.get('https://alpha-meme-maker.herokuapp.com')
    json_data = json.loads(response.text)
    #api is limited in size and ony has 54 memes
    meme = json_data['data'][random.randrange(1, 54)]['image'] 
    return meme


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
    author = str(message.author)

# bot functions
    if msg.startswith('$hello'):
        await message.channel.send('Nameste!')

    if msg.startswith('$introduce'):
        await message.channel.send('I am you dad @' + author)

    if msg.startswith('$gyan'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$roast'):
        insult = evil_insult()
        await message.channel.send(insult)

    if msg.startswith('$meme'):
        meme = get_meme()
        await message.channel.send("Here is a low effort meme for you-")
        await message.channel.send(meme)


# anti curse features
    if any(word in msg for word in curse_en):
        await message.channel.send(random.choice(anti_curse_en))
    elif any(word in msg for word in curse_hi):
        await message.channel.send(random.choice(anti_curse_hi))

'''@client.command(name="com")
async def _command(ctx):
    global times_used
    await ctx.send(f"y or n")

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["y", "n"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "y":
        await ctx.send("You said yes!")
    else:
        await ctx.send("You said no!")

    times_used = times_used + 1   
    '''   

keep_alive()
client.run(TOKEN)