import requests

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/people/<name>", methods=["GET"])
def people(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/people?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/films/<name>", methods=["GET"])
def films(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/films?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/planets/<name>", methods=["GET"])
def planets(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/planets?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/starships/<name>", methods=["GET"])
def starships(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/starships?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/all/<name>", methods=["GET"])
def all_items(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    list_people = people(name)
    list_films = films(name)
    list_planets = planets(name)
    list_starships = starships(name)

    return list_people + list_films + list_planets + list_starships
