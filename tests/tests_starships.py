from app.main import get_starships


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
