from flask import Flask, render_template, url_for, request, jsonify
import requests


app = Flask(__name__)

from grandpybot_app import get_loc, get_title, get_info, parse_entry, papy_style

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    userentry = request.form['userentry']
    key = app.config['GOOGLE_API_KEY']
    keywords = parse_entry(userentry)
    if keywords:
        place = get_loc(keywords, key)
        if place:
            title = get_title(place['name'])
        else:
            return "noplace"
        place['info'] = get_info(title, 3)
        place = papy_style(place)
        return jsonify(place)
    else:
        return "nothing"
