def _get_allergens_and_ingredients(filename):
    allergens_dict = {}
    all_ingredients = []
    for line in open(filename):
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        all_ingredients += ingredients
        allergens = allergens.strip(')\n')
        for allergen in allergens.split(', '):
            if allergen in allergens_dict:
                old_allergens = allergens_dict[allergen]
                allergens_dict[allergen] = [x for x in old_allergens if x in ingredients]
            else:
                allergens_dict[allergen] = ingredients
    return allergens_dict, all_ingredients


def test_part_one():
    assert part_one('./21/example-input.txt') == 5


def part_one(filename):
    allergens_dict, all_ingredients = _get_allergens_and_ingredients(filename)
    all_allergens = []
    for allergens in allergens_dict.values():
        all_allergens += allergens
    return len([ingredient for ingredient in all_ingredients if ingredient not in all_allergens])


def test_part_two():
    assert part_two('./21/example-input.txt') == 'mxmxvkd,sqjhc,fvjkl'


def part_two(filename):
    allergens_dict, _ = _get_allergens_and_ingredients(filename)
    found_ingredients = []
    while len(found_ingredients) < len(allergens_dict.keys()):
        for allergen, ingredients in allergens_dict.items():
            if len(ingredients) == 1:
                found_ingredients.append(ingredients[0])
            else:
                allergens_dict[allergen] = [x for x in ingredients if x not in found_ingredients]
                if len(allergens_dict[allergen]) == 1:
                    found_ingredients.append(ingredients[0])
    allergens = [allergens_dict[x][0] for x in sorted(allergens_dict)]
    return ','.join(allergens)


if __name__ == '__main__':
    test_part_one()
    print("Part one answer: {}".format(part_one('./21/input.txt')))
    test_part_two()
    print("Part two answer: {}".format(part_two('./21/input.txt')))