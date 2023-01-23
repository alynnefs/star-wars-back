import requests
from typing import List, Dict


def get_items(sub_url: str) -> Dict:
    # TODO: resolver para mais de um item obtido
    url_base = "https://swapi.dev/api"
    response = requests.get(f"{url_base}/{sub_url}")
    data = response.json()

    return data


def find_characters(characters: List) -> List:
    from app.main import get_people_by_id

    character1_id = characters[0].split("/")[-2]
    character1 = get_people_by_id(character1_id)

    character2_id = characters[1].split("/")[-2]
    character2 = get_people_by_id(character2_id)

    character3_id = characters[2].split("/")[-2]
    character3 = get_people_by_id(character3_id)

    return [character1, character2, character3]


def find_recommendations(items: List[Dict]) -> List:
    recommendations_per_item = []
    for item in items:
        recommendations = []
        characters = item.get("characters")
        if characters:
            recommendations = find_characters(characters)
        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )

    return recommendations_per_item
