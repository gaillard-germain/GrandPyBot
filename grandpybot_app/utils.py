import requests
import re
import json
from random import choice


class Seeker():
    @staticmethod
    def get_loc(query, key):
        """Gets name and address of a place with a query using
           a request to gooleapis (needs a valid token)"""

        url = "https://maps.googleapis.com/maps/api/place/\
findplacefromtext/json"
        params = {"input": query,
                  "inputtype": "textquery",
                  "language": "fr",
                  "fields": "name,formatted_address",
                  "key": key}
        embed_url = "https://www.google.com/maps/embed/v1/place"
        response = requests.get(url=url, params=params)
        data = response.json()
        loc = {}
        if data['status'] == "OK":
            loc['name'] = data['candidates'][0]['name']
            loc['address'] = data['candidates'][0]['formatted_address']
            loc['source'] = "{}?q={}&key={}".format(embed_url, query, key)
        return loc

    @staticmethod
    def get_title(query):
        """Gets an article's title with a query to wiki media api"""

        url = "https://fr.wikipedia.org/w/api.php"
        params = {"action": "query",
                  "format": "json",
                  "list": "search",
                  "srsearch": query}
        response = requests.get(url=url, params=params)
        data = response.json()
        title = data['query']['search'][0]['title']
        return title

    @staticmethod
    def get_info(title, sentence_number):
        """Extracts n sentences from wikipedia article using its title"""

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


class Former():
    @staticmethod
    def parse_entry(entry):
        """Parses a string to isolate keywords"""

        with open('grandpybot_app/data/unwanted.json') as data:
            unwanted = json.load(data)
        entry = re.split(r'\W+|\d+', entry.lower())
        result = []
        for word in entry:
            if word and word not in unwanted:
                result.append(word)
        result = ' '.join(result)
        return result

    @staticmethod
    def papy_style(place):
        """Adds a random sentences to a dict string value"""

        with open('grandpybot_app/data/papy.json') as data:
            papy = json.load(data)
        place['name'] = choice(papy['start']).format(place['name'])
        place['info'] = choice(papy['end']).format(place['info'])
        return place
