import requests


def get_loc(query, key):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {"input": query,
              "inputtype": "textquery",
              "fields": "name,formatted_address,geometry",
              "key": key}
    response = requests.get(url=url, params=params)
    data = response.json()
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
