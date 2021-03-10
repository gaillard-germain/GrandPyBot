import requests


class Seeker():
    @staticmethod
    def get_loc(query, key):
        """Gets name and address of a place with a query using
           a request to googleapis (needs a valid token)"""

        url = "https://maps.googleapis.com/maps/api/place/\
findplacefromtext/json"
        params = {"input": query,
                  "inputtype": "textquery",
                  "language": "fr",
                  "fields": "name,formatted_address",
                  "key": key}
        embed_url = "https://www.google.com/maps/embed/v1/place?q={}&key={}"
        response = requests.get(url=url, params=params)
        data = response.json()
        loc = {}
        if data['status'] == "OK":
            loc['name'] = data['candidates'][0]['name']
            loc['address'] = data['candidates'][0]['formatted_address']
            loc['source'] = embed_url.format(loc['name'].lower(), key)
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
        if data['query']['searchinfo']['totalhits']:
            title = data['query']['search'][0]['title']
            return title
        else:
            return query

    @staticmethod
    def get_info(title, sentence_number):
        """Extracts n sentences from wikipedia article using its title"""

        url = "https://fr.wikipedia.org/w/api.php"
        params = {"action": "query",
                  "format": "json",
                  "prop": "extracts",
                  "titles": title,
                  "exsentences": sentence_number,
                  "exlimit": "1",
                  "explaintext": "1",
                  "formatversion": "2"}
        response = requests.get(url=url, params=params)
        data = response.json()
        try:
            return data['query']['pages'][0]['extract']
        except KeyError:
            return "...ah ma mémoire me fait défaut."
