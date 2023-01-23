from app.main import (
    get_people,
    get_films,
    get_planets,
    get_starships,
    get_all_items,
)

from app.recommendations import find_recommendations


def test_get_people():
    response = get_people("R5-D4")
    people = response[0].get("item")
    assert people["name"] == "R5-D4"


def test_get_films():
    response = get_films("A New Hope")
    film = response[0].get("item")
    assert film["title"] == "A New Hope"


def test_get_recommendations_for_film():
    response = get_films("A New Hope")
    recommendations = response[0].get("recommendations")

    assert recommendations[0]["name"] == "Luke Skywalker"
    assert recommendations[1]["name"] == "C-3PO"
    assert recommendations[2]["name"] == "R2-D2"


def test_get_more_than_one_film():
    films = get_films("the")

    assert films[0]["item"]["title"] == "The Empire Strikes Back"
    assert films[1]["item"]["title"] == "Return of the Jedi"
    assert films[2]["item"]["title"] == "The Phantom Menace"
    assert films[3]["item"]["title"] == "Attack of the Clones"
    assert films[4]["item"]["title"] == "Revenge of the Sith"


def test_recommendations_for_more_than_one_film():
    films = get_films("the")

    film_recommendations_0 = films[0]["recommendations"]
    assert film_recommendations_0[0]["name"] == "Luke Skywalker"
    assert film_recommendations_0[1]["name"] == "C-3PO"
    assert film_recommendations_0[2]["name"] == "R2-D2"

    film_recommendations_1 = films[1]["recommendations"]
    assert film_recommendations_1[0]["name"] == "Luke Skywalker"
    assert film_recommendations_1[1]["name"] == "C-3PO"
    assert film_recommendations_1[2]["name"] == "R2-D2"

    film_recommendations_2 = films[2]["recommendations"]
    assert film_recommendations_2[0]["name"] == "C-3PO"
    assert film_recommendations_2[1]["name"] == "R2-D2"
    assert film_recommendations_2[2]["name"] == "Obi-Wan Kenobi"

    film_recommendations_3 = films[3]["recommendations"]
    assert film_recommendations_3[0]["name"] == "C-3PO"
    assert film_recommendations_3[1]["name"] == "R2-D2"
    assert film_recommendations_3[2]["name"] == "Owen Lars"

    film_recommendations_4 = films[4]["recommendations"]
    assert film_recommendations_4[0]["name"] == "Luke Skywalker"
    assert film_recommendations_4[1]["name"] == "C-3PO"
    assert film_recommendations_4[2]["name"] == "R2-D2"


def test_get_planets():
    response = get_planets("Naboo")
    planets = response.get("item")
    assert planets[0]["name"] == "Naboo"


def test_get_starships():
    response = get_starships("Death Star")
    starships = response.get("item")
    assert starships[0]["name"] == "Death Star"


def test_all_items():
    response = get_all_items("naboo")
    items = response.get("item")

    # planet
    assert items[0]["name"] == "Naboo"

    # starships
    assert items[1]["name"] == "Naboo fighter"
    assert items[2]["name"] == "Naboo Royal Starship"
    assert items[3]["name"] == "Naboo star skiff"
