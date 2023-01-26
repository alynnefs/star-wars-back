from app.main import get_planets


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
