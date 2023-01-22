def find_characters(characters):
    from app.main import get_people_by_id

    character1_id = characters[0].split("/")[-2]
    character1 = get_people_by_id(character1_id)

    character2_id = characters[1].split("/")[-2]
    character2 = get_people_by_id(character2_id)

    character3_id = characters[2].split("/")[-2]
    character3 = get_people_by_id(character3_id)

    return [character1, character2, character3]


def find_recommendations(items):
    recommendations = []
    for item in items:
        characters = item.get("characters")
        if characters:
            recommendations = find_characters(characters)
    return recommendations
