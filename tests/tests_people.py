from app.main import get_people


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
