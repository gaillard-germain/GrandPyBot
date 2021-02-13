import requests


def get_place_info(query, key):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=name,formatted_address,geometry&key={}".format(query, key)
    places = requests.get(url)
    places = places.json()
    place = places['candidates'][0]
    place_info = {'question': query,
                  'name': place['name'],
                  'address': place['formatted_address'],
                  'source': "https://www.google.com/maps/embed/v1/place?q={}&key={}".format(query, key)}
    return place_info
