from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

from grandpybot_app import Seeker, Rhetoric

app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/answer', methods=['POST'])
def answer():
    userentry = request.form['userentry']
    key = app.config['GOOGLE_API_KEY']
    keywords = Rhetoric.parse_entry(userentry)
    if keywords:
        place = Seeker.get_loc(keywords, key)
        if place:
            title = Seeker.get_title(keywords)
        else:
            return "noplace"
        place['info'] = Seeker.get_info(title, 3)
        place = Rhetoric.papy_style(place)
        return jsonify(place)
    else:
        return "nothing"
