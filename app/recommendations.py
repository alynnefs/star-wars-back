# TODO: encontrar nome melhor


def find_characters(characters):
    from app.main import people_id

    character1_id = characters[0].split("/")[-2]
    character1 = people_id(character1_id)

    character2_id = characters[1].split("/")[-2]
    character2 = people_id(character2_id)

    character3_id = characters[2].split("/")[-2]
    character3 = people_id(character3_id)

    return [character1, character2, character3]


def find_recommendations(items):
    recommendations = []
    for item in items:
        if item.get("characters"):
            recommendations = find_characters(item["characters"])
    return recommendations
