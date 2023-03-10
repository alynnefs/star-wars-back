from flask import Flask, request
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

default_response = []


@app.route("/people/", methods=["GET"])
@app.route("/people/<name>", methods=["GET"])
def get_people(name=""):
    if not name:
        return default_response

    sub_url = f"people?search={name}"
    data = get_items(sub_url)

    return find_recommendations_people(data.get("results")) or default_response


@app.route("/films/", methods=["GET"])
@app.route("/films/<name>", methods=["GET"])
def get_films(name=""):
    if not name:
        return default_response

    sub_url = f"films?search={name}"
    data = get_items(sub_url)

    return find_recommendations_film(data.get("results")) or default_response


@app.route("/planets/", methods=["GET"])
@app.route("/planets/<name>", methods=["GET"])
def get_planets(name=""):
    if not name:
        return default_response

    sub_url = f"planets?search={name}"
    data = get_items(sub_url)

    return find_recommendations_planets(data.get("results")) or default_response


@app.route("/starships/", methods=["GET"])
@app.route("/starships/<name>", methods=["GET"])
def get_starships(name=""):
    if not name:
        return default_response

    sub_url = f"starships?search={name}"
    data = get_items(sub_url)

    return find_recommendations_starships(data.get("results")) or default_response


@app.route("/all/", methods=["GET"])
@app.route("/all/<name>", methods=["GET"])
def get_all_items(name=""):
    """
    Get all items that fit the pattern.
    It can have more than one type of item.
    """
    if not name:
        return default_response

    response = []

    people = get_people(name)
    films = get_films(name)
    planets = get_planets(name)
    starships = get_starships(name)

    # The += is used to sum the items within the list,
    # not the entire list
    if people:
        response += people
    if films:
        response += films
    if planets:
        response += planets
    if starships:
        response += starships

    return response or default_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
