from flask import Flask

from app.recommendations import get_items, find_recommendations

app = Flask(__name__)


@app.route("/")
def hello_world():
    # TODO: fazer tela padrão
    return "<p>Hello, World!</p>"


@app.route("/people/<name>", methods=["GET"])
def get_people(name):
    sub_url = f"people?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations(data.get("results"))

    return recommendations_per_item or {"item": []}


@app.route("/films/<name>", methods=["GET"])
def get_films(name):
    sub_url = f"films?search={name}"
    data = get_items(sub_url)

    recommendations_per_item = find_recommendations(data.get("results"))

    return recommendations_per_item or {"item": []}


@app.route("/planets/<name>", methods=["GET"])
def get_planets(name):
    sub_url = f"planets?search={name}"
    data = get_items(sub_url)

    return {"item": data.get("results")}


@app.route("/starships/<name>", methods=["GET"])
def get_starships(name):
    sub_url = f"starships?search={name}"
    data = get_items(sub_url)

    return {"item": data.get("results")}


@app.route("/all/<name>", methods=["GET"])
def get_all_items(name):
    # TODO: para cada item encontrado, 3 recomendações?
    response = []

    people = get_people(name)
    films = get_films(name)
    planets = get_planets(name)
    starships = get_starships(name)

    response = (
        people.get("item")
        + films.get("item")
        + planets.get("item")
        + starships.get("item")
    )

    return {"item": response}


@app.route("/people/<people_id>", methods=["GET"])
def get_people_by_id(people_id):
    sub_url = f"people/{people_id}"
    data = get_items(sub_url)

    return data


@app.route("/films/<film_id>", methods=["GET"])
def get_film_by_id(film_id):
    sub_url = f"films/{film_id}"
    data = get_items(sub_url)

    return data
