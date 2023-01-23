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


def find_items(count, items: List) -> List:
    recommendations = []
    for item in items:
        if count >= 3:
            break

        recommendations.append(get_item_by_link(item))
        count += 1

    return count, recommendations


def find_recommendations(items: List[Dict]) -> List[Dict]:
    recommendations_per_item = []
    for item in items:
        count = 0

        recommendations = []
        if item.get("characters"):
            count, recommendations = find_items(count, item.get("characters"))

        if count < 3 and item.get("films"):
            count, recommendations = find_items(count, item.get("films"))

        if count < 3 and item.get("starships"):
            count, recommendations = find_items(count, item.get("films"))

        if count < 3 and item.get("homeworld"):
            count, recommendations = find_items(count, item.get("films"))

        if count < 3 and item.get("starship_class"):
            count, recommendations = find_items(count, item.get("films"))

        if count < 3 and item.get("manufacturer"):
            count, recommendations = find_items(count, item.get("films"))

        if count < 3 and item.get("residents"):
            count, recommendations = find_items(count, item.get("films"))

        recommendations_per_item.append(
            {"item": item, "recommendations": recommendations}
        )

    return recommendations_per_item
