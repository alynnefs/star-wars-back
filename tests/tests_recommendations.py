from app.recommendations import find_recommendations

def test_get_recommendations_for_film():
    from app.main import films
    films_obtained = films("A New Hope")
    recommendations = []
    for film in films_obtained:
        recommendations = find_recommendations(film)

    assert recommendations[0]['name'] == 'Luke Skywalker'
    assert recommendations[1]['name'] == 'C-3PO'
    assert recommendations[2]['name'] == 'R2-D2'
