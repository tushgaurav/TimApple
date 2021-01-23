import discord
import requests
import json
import time
import random
import csv
import wolframalpha
from decouple import config
from keep_alive import keep_alive

TOKEN = config('TOKEN') #discord token from env
app_id = config('APP_ID') #wolfram alpha app id from env
wolfram = wolframalpha.Client(app_id)

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
    
    "Courage is fire, and bullying is smoke.",
    "Not all forms of abuse leave bruises.",
    
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
    "शरीफों की शराफत और हमारा,कमीनापन किसी को अच्छा, नहीं लगता!!",
    "lol XD mai kaise maan lu?"
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

def ask_que(question):
    res = wolfram.query(question)
    answer = next(res.results).text
    return answer


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
    await client.change_presence(activity=discord.Game('iPhone 13 Pro Max'))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    author = (message.author)
    previous_status = client.guilds[0].get_member(client.user.id).activity

# bot functions
    if msg.startswith('$hello'):
        await message.channel.send('Nameste!')

    if msg.startswith('$introduce'):
        await message.channel.send('I am your dad ' + author.mention)

    if msg.startswith('$gyan'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$roast'):
        insult = evil_insult()
        await message.channel.send(insult)

    if msg.startswith('$meme'):
        await message.channel.send("You are a living meme.")

    if msg.startswith('$ask'):
        question = msg[5:]
        res = ask_que(question)
        await message.channel.send(res)

    if msg.startswith('$listen'):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='to sad noises!'))
        await message.channel.send("I am now listening to sad noises") 
        time.sleep(10)
        await client.change_presence(activity=previous_status)  

    #if msg.startswith('$time'):    

# anti curse features
    if any(word in msg for word in curse_en):
        await message.channel.send(random.choice(anti_curse_en))
    elif any(word in msg for word in curse_hi):
        await message.channel.send(random.choice(anti_curse_hi))
 

keep_alive()

client.run(TOKEN)