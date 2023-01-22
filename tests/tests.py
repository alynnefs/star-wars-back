from app.main import (
    people,
    films,
    planets,
    starships,
    all_items,
)


def test_get_people():
    people_obtained = people("Luke")
    assert people_obtained[0]["name"] == "Luke Skywalker"


def test_get_films():
    films_obtained = films("A New Hope")
    assert films_obtained[0]["title"] == "A New Hope"


def test_get_more_than_one_film():
    films_obtained = films("the")
    assert films_obtained[0]["title"] == "The Empire Strikes Back"
    assert films_obtained[1]["title"] == "Return of the Jedi"
    assert films_obtained[2]["title"] == "The Phantom Menace"
    assert films_obtained[3]["title"] == "Attack of the Clones"
    assert films_obtained[4]["title"] == "Revenge of the Sith"


def test_get_planets():
    planets_obtained = planets("Naboo")
    assert planets_obtained[0]["name"] == "Naboo"


def test_get_starships():
    starships_obtained = starships("Death Star")
    assert starships_obtained[0]["name"] == "Death Star"


def test_all_items():
    items_obtained = all_items("naboo")

    # planet
    assert items_obtained[0]["name"] == "Naboo"

    # starships
    assert items_obtained[1]["name"] == "Naboo fighter"
    assert items_obtained[2]["name"] == "Naboo Royal Starship"
    assert items_obtained[3]["name"] == "Naboo star skiff"
