from app.main import get_people, get_planets, get_films, get_starships, get_all_items


def test_no_parameter_people():
    response = get_people("")
    assert response == []


def test_no_parameter_planets():
    response = get_planets("")
    assert response == []


def test_no_parameter_films():
    response = get_films("")
    assert response == []


def test_no_parameter_starships():
    response = get_starships("")
    assert response == []


def test_no_parameter_all_items():
    response = get_all_items("")
    assert response == []
