from app.main import get_films


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
