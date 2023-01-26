from flask import Flask
from flask_cors import CORS

from app.recommendations import (
    get_items,
    find_recommendations_people,
    find_recommendations_film,
    find_recommendations_starships,
    find_recommendations_planets,
)

app = Flask(__name__)
CORS(app, support_credentials=True)

default_response = [{"item": [], "recommendations": []}]


@app.route("/people/<name>", methods=["GET"])
def get_people(name):
    sub_url = f"people?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations_people(data.get("results"))

    return recommendations_per_item or default_response


@app.route("/films/<name>", methods=["GET"])
def get_films(name):
    sub_url = f"films?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations_film(data.get("results"))

    return recommendations_per_item or default_response


@app.route("/planets/<name>", methods=["GET"])
def get_planets(name):
    sub_url = f"planets?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations_planets(data.get("results"))

    return recommendations_per_item or default_response


@app.route("/starships/<name>", methods=["GET"])
def get_starships(name):
    sub_url = f"starships?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations_starships(data.get("results"))

    return recommendations_per_item or default_response


@app.route("/all/<name>", methods=["GET"])
def get_all_items(name):
    """
    Get all items that fit the pattern.
    It can have more than one type of item.
    """
    response = []

    people = get_people(name)
    films = get_films(name)
    planets = get_planets(name)
    starships = get_starships(name)

    # The += is used to sum the items within the list,
    # not the entire list
    if people[0].get("item"):
        response += people
    if films[0].get("item"):
        response += films
    if planets[0].get("item"):
        response += planets
    if starships[0].get("item"):
        response += starships

    return response or default_response
