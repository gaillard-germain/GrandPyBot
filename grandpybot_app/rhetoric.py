import re
import json
from random import choice


class Rhetoric():
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
