from app.main import get_all_items


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
    """
    planet and starships
    """
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


def test_all_items_people_and_recommendations():
    response = get_all_items("R2-D2")

    items = response[0].get("item")
    assert items["name"] == "R2-D2"

    recommendations = response[0].get("recommendations")

    assert recommendations[0]["name"] == "Luke Skywalker"
    assert recommendations[1]["name"] == "C-3PO"
    assert recommendations[2]["name"] == "Darth Vader"


def test_all_items_film_and_recommendations():
    response = get_all_items("A New Hope")

    items = response[0].get("item")
    assert items["title"] == "A New Hope"

    recommendations = response[0].get("recommendations")
    assert recommendations[0]["title"] == "The Empire Strikes Back"
    assert recommendations[1]["title"] == "Return of the Jedi"
    assert recommendations[2]["title"] == "Revenge of the Sith"
