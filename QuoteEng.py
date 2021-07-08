import csv
import random
import html

# number of rows in the csv files, needs to be updated if addition is made to the database
jokesSize = 38270
jokes_hiSize = 22
helloSize = 143

# jokes.csv obtained from r/Jokes (subreddit), jokes_hi.csv is obtained from publically available data and hello-salut.csv from publically available data
with open('./data/jokes.csv', encoding='utf8') as file:
    jokes = csv.DictReader(file)
    joke = list(jokes)

with open('./data/jokes_hi.csv', encoding='utf8') as file:
    jokes = csv.DictReader(file)
    joke_hi = list(jokes)

with open('./data/hello-salut.csv', encoding='utf8') as file:
    reader = csv.DictReader(file)
    hello_list = list(reader)


# function returns a list of random question and answer from the jokes.csv file
def qandaJokes():
    randNum = random.randint(1, jokesSize - 2)
    returnList = [joke[randNum]['Question'], joke[randNum]['Answer']]
    return returnList


# function returns a random string from the jokes_hi.csv file
def hindiJokes():
    randNum = random.randint(1, jokes_hiSize - 2)
    print(randNum)
    return joke_hi[randNum]['Joke']

# function return a hello in different language in the format like "Nameste from India!"
def salut():
    randNum = random.randint(1, helloSize - 2)
    hello = [html.unescape(hello_list[randNum]['hello']),
             hello_list[randNum]['country']]
    return hello
