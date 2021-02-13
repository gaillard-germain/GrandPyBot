from flask import Flask, render_template, url_for, request, jsonify
import requests


app = Flask(__name__)

from grandpybot_app import get_place_info

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    userentry = request.form['userentry']
    key = app.config['GOOGLE_API_KEY']
    place = get_place_info(userentry, key)
    return jsonify(place)
