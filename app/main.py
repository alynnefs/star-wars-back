import requests

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    # TODO: fazer tela padrão
    return "<p>Hello, World!</p>"


@app.route("/people/<name>", methods=["GET"])
def get_people(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/people?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/films/<name>", methods=["GET"])
def get_films(name):
    from app.recommendations import find_recommendations

    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/films?search={name}")
    data = response.json()
    results = data.get("results")

    recommendations = find_recommendations(results)
    return {"item": results, "recommendations": recommendations}


@app.route("/planets/<name>", methods=["GET"])
def get_planets(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/planets?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/starships/<name>", methods=["GET"])
def get_starships(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/starships?search={name}")
    data = response.json()
    return data.get("results")


@app.route("/all/<name>", methods=["GET"])
def get_all_items(name):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    list_people = get_people(name)
    list_films = get_films(name)
    list_planets = get_planets(name)
    list_starships = get_starships(name)

    return list_people + list_films + list_planets + list_starships


@app.route("/people/<people_id>", methods=["GET"])
def get_people_by_id(people_id):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/people/{people_id}")
    data = response.json()
    return data


@app.route("/films/<film_id>", methods=["GET"])
def get_film_by_id(film_id):
    # TODO: generalizar url_base
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/films/{film_id}")
    data = response.json()
    return data
