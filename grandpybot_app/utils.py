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
    if data['status'] == "OK":
        loc = {'name': data['candidates'][0]['name'],
               'address': data['candidates'][0]['formatted_address'],
               'source': "https://www.google.com/maps/embed/v1/place?q={}&key={}".format(query, key)}
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

def parse_entry():
    with open('json/fr.json') as data:
        unwanted = json.load(data)
    entry = "dit moi papy... sais-tu ou ce trouve l'adresse de l'opera de Paris?"
    pattern = re.compile(r'(\badresse\s)+(\bde la\s|\bdu\s|\bd\W|\bde l\W)', re.IGNORECASE)
    begin = pattern.search(entry).end()
    entry = entry[begin:]
    entry = re.split('\W+', entry)
    for word in entry:
        if word in unwanted:
            entry.remove(word)
    entry = ' '.join(entry[:-1])
    print(entry)

if __name__ == '__main__':
    parse_entry()
