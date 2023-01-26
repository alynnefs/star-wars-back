import requests
from typing import List, Dict


def get_items(sub_url: str) -> Dict:
    # TODO: resolver para mais de um item obtido
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/{sub_url}")
    data = response.json()

    return data


def get_item_by_link(link):
    response = requests.get(link)
    data = response.json()

    return data


def find_recommendations_starships(items: List) -> List:
    # TODO: check cases with less than 3 recommendations
    recommendations_per_item = []
    for item in items:
        count = 0
        recommendations = []

        url_film = item.get("films")[0]
        film = get_item_by_link(url_film)
        url_starships = film.get("starships")

        for url in url_starships:
            if count == 3:
                break
            if url != item.get("url"):
                starship = get_item_by_link(url)
                recommendations.append(starship)
                count += 1

        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )
    return recommendations_per_item


def find_recommendations_people(items: List[Dict]) -> List[Dict]:
    recommendations_per_item = []
    for item in items:
        count = 0
        recommendations = []

        url_film = item.get("films")[0]
        film = get_item_by_link(url_film)
        url_characters = film.get("characters")

        for url in url_characters:
            if count == 3:
                break
            if url != item.get("url"):
                character = get_item_by_link(url)
                recommendations.append(character)
                count += 1

        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )
    return recommendations_per_item


def find_recommendations_film(items: List[Dict]) -> List[Dict]:
    recommendations_per_item = []
    for item in items:
        count = 0
        recommendations = []

        url_character = item.get("characters")[0]
        character = get_item_by_link(url_character)
        url_films = character.get("films")
        for url in url_films:
            if count == 3:
                break
            if url != item.get("url"):
                film = get_item_by_link(url)
                recommendations.append(film)
                count += 1

        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )
    return recommendations_per_item


def find_recommendations_planets(items: List[Dict]) -> List[Dict]:
    recommendations_per_item = []
    for item in items:
        count = 0
        recommendations = []

        url_film = item.get("films")[0]
        film = get_item_by_link(url_film)
        url_planets = film.get("planets")

        for url in url_planets:
            if count == 3:
                break
            if url != item.get("url"):
                character = get_item_by_link(url)
                recommendations.append(character)
                count += 1

        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )

    return recommendations_per_item
