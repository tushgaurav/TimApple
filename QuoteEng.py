import csv
import random

# number of rows in the csv files
jokesSize = 38270
jokes_hiSize = 22

# jokes.csv obtained from r/Jokes and jokes_hi.csv is obtained from publically available data
with open('./data/jokes.csv', encoding='utf8') as file:
    jokes = csv.DictReader(file)
    joke = list(jokes)

with open('./data/jokes_hi.csv', encoding='utf8') as file:
    jokes = csv.DictReader(file)
    joke_hi = list(jokes)


# function returns a list of random question and answer from the jokes.csv file
def qandaJokes():
    randNum = random.randint(1, jokesSize - 1)
    returnList = [joke[randNum]['Question'], joke[randNum]['Answer']]
    return returnList

# function returns a random string from the jokes_hi.csv file


def hindiJokes():
    randNum = random.randint(1, jokes_hiSize - 1)
    return joke_hi[randNum]['Joke']
