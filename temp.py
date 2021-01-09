import json
import requests


def evil_insult():
    response = requests.get(
        'https://evilinsult.com/generate_insult.php?lang=en&type=json')
    json_data = json.loads(response.text)
    insult = json_data['insult']
    return(insult)


print(evil_insult())
