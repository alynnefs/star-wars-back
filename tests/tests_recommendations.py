from app.main import (
    get_people,
    get_films,
    get_planets,
    get_starships,
    get_all_items,
)


def test_get_people():
    response = get_people("R5-D4")
    people = response[0].get("item")
    assert people["name"] == "R5-D4"


def test_get_recommendations_for_people():
    """
    Characters in the same film
    """
    response = get_people("luke")

    recommendations = response[0].get("recommendations")
    assert recommendations[0]["name"] == "C-3PO"
    assert recommendations[1]["name"] == "R2-D2"
    assert recommendations[2]["name"] == "Darth Vader"


def test_get_films():
    response = get_films("A New Hope")
    film = response[0].get("item")
    assert film["title"] == "A New Hope"


def test_get_recommendations_for_film():
    """
    Films with the same character
    """
    response = get_films("A New Hope")
    recommendations = response[0].get("recommendations")

    assert recommendations[0]["title"] == "The Empire Strikes Back"
    assert recommendations[1]["title"] == "Return of the Jedi"
    assert recommendations[2]["title"] == "Revenge of the Sith"


def test_get_more_than_one_film():
    films = get_films("the")

    assert films[0]["item"]["title"] == "The Empire Strikes Back"
    assert films[1]["item"]["title"] == "Return of the Jedi"
    assert films[2]["item"]["title"] == "The Phantom Menace"
    assert films[3]["item"]["title"] == "Attack of the Clones"
    assert films[4]["item"]["title"] == "Revenge of the Sith"


def test_recommendations_for_more_than_one_film():
    """
    Films with the same character for each film
    """
    films = get_films("the")

    film_recommendations_0 = films[0]["recommendations"]
    assert film_recommendations_0[0]["title"] == "A New Hope"
    assert film_recommendations_0[1]["title"] == "Return of the Jedi"
    assert film_recommendations_0[2]["title"] == "Revenge of the Sith"

    film_recommendations_1 = films[1]["recommendations"]
    assert film_recommendations_1[0]["title"] == "A New Hope"
    assert film_recommendations_1[1]["title"] == "The Empire Strikes Back"
    assert film_recommendations_1[2]["title"] == "Revenge of the Sith"

    film_recommendations_2 = films[2]["recommendations"]
    assert film_recommendations_2[0]["title"] == "A New Hope"
    assert film_recommendations_2[1]["title"] == "The Empire Strikes Back"
    assert film_recommendations_2[2]["title"] == "Return of the Jedi"

    film_recommendations_3 = films[3]["recommendations"]
    assert film_recommendations_3[0]["title"] == "A New Hope"
    assert film_recommendations_3[1]["title"] == "The Empire Strikes Back"
    assert film_recommendations_3[2]["title"] == "Return of the Jedi"

    film_recommendations_4 = films[4]["recommendations"]
    assert film_recommendations_4[0]["title"] == "A New Hope"
    assert film_recommendations_4[1]["title"] == "The Empire Strikes Back"
    assert film_recommendations_4[2]["title"] == "Return of the Jedi"


def test_get_planets():
    response = get_planets("Naboo")
    planets = response[0].get("item")
    assert planets["name"] == "Naboo"


def test_get_recommendations_for_planets():
    """
    Planets in the same film
    """
    response = get_planets("Naboo")
    recommendations = response[0].get("recommendations")

    assert recommendations[0]["name"] == "Tatooine"
    assert recommendations[1]["name"] == "Dagobah"
    assert recommendations[2]["name"] == "Endor"


def test_get_starships():
    response = get_starships("Death Star")
    starships = response[0].get("item")
    assert starships["name"] == "Death Star"


def test_get_recommendations_for_starships():
    """
    Starships in the same film
    """
    response = get_starships("Death Star")
    recommendations = response[0].get("recommendations")

    assert recommendations[0]["name"] == "CR90 corvette"
    assert recommendations[1]["name"] == "Star Destroyer"
    assert recommendations[2]["name"] == "Sentinel-class landing craft"


def test_all_items():
    response = get_all_items("naboo")

    items_0 = response[0].get("item")
    items_1 = response[1].get("item")
    items_2 = response[2].get("item")
    items_3 = response[3].get("item")

    # planet
    assert items_0["name"] == "Naboo"

    # starships
    assert items_1["name"] == "Naboo fighter"
    assert items_2["name"] == "Naboo Royal Starship"
    assert items_3["name"] == "Naboo star skiff"


def test_get_recommendations_for_all_items():
    response = get_all_items("naboo")

    # planet
    recommendations_0 = response[0].get("recommendations")
    assert recommendations_0[0]["name"] == "Tatooine"
    assert recommendations_0[1]["name"] == "Dagobah"
    assert recommendations_0[2]["name"] == "Endor"

    # starships
    recommendations_1 = response[1].get("recommendations")
    assert recommendations_1[0]["name"] == "Republic Cruiser"
    assert recommendations_1[1]["name"] == "Droid control ship"
    assert recommendations_1[2]["name"] == "Naboo Royal Starship"

    recommendations_2 = response[2].get("recommendations")
    assert recommendations_2[0]["name"] == "Republic Cruiser"
    assert recommendations_2[1]["name"] == "Droid control ship"
    assert recommendations_2[2]["name"] == "Naboo fighter"

    recommendations_3 = response[3].get("recommendations")
    assert recommendations_3[0]["name"] == "CR90 corvette"
    assert recommendations_3[1]["name"] == "Droid control ship"
    assert recommendations_3[2]["name"] == "Jedi starfighter"
