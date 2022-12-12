def transform_weapons(weapons):
    return [transform_weapon(weapon) for weapon in weapons]


def transform_weapon(weapon):
    name = weapon['status']['info']['name']
    description = weapon['description']
    availability = weapon['availability']
    characteristics = weapon['characteristics']
    move_set = [value for value in weapon['move_set'].values()]

    return (
        name,
        description,
        ' '.join(availability) if availability else '',
        ' '.join(characteristics) if characteristics else '',
        ' '.join(move_set) if move_set else ''
    )
