import requests
import re
import json


def get_loc(query, key):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {"input": query,
              "inputtype": "textquery",
              "language": "fr",
              "fields": "name,formatted_address",
              "key": key}
    response = requests.get(url=url, params=params)
    data = response.json()
    loc = {}
    if data['status'] == "OK":
        loc['name'] = data['candidates'][0]['name']
        loc['address'] = data['candidates'][0]['formatted_address']
        loc['source'] = "https://www.google.com/maps/embed/v1/place?q={}&key={}".format(query, key)
    return loc

def get_title(query):
    url = "https://fr.wikipedia.org/w/api.php"
    params = {"action": "query",
              "format": "json",
              "list": "search",
              "srsearch": query}
    response = requests.get(url=url, params=params)
    data = response.json()
    title = data['query']['search'][0]['title']
    return title

def get_info(title, sentence_number):
    url = "https://fr.wikipedia.org/w/api.php"
    params = {"action": "query",
              "format": "json",
              "prop": "extracts",
              "exsentences": sentence_number,
              "exlimit": "1",
              "titles": title,
              "explaintext": "1",
              "formatversion": "2"}
    response = requests.get(url=url, params=params)
    data = response.json()
    return data['query']['pages'][0]['extract']

def parse_entry(entry):
    with open('grandpybot_app/data/unwanted.json') as data:
        unwanted = json.load(data)
    entry = re.split(r'\W+|\d+', entry.lower())
    result = []
    for word in entry:
        if word and word not in unwanted:
            result.append(word)
    result = ' '.join(result)
    return result

def papy_style(place):
    place['name'] = "Bien sûr mon crapaud, {}, ce trouve: ".format(place['name'])
    place['info'] = "A ce propos t'ai je déja dit que: {}".format(place['info'])
    return place
