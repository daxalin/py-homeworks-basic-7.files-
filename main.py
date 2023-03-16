from pprint import pprint
with open('recipes.txt', 'r', encoding = "utf-8") as file:
    recipes = {}
    for line in file:
        recipe_name = line.strip()
        eng_count = int(file.readline())
        ingridients = []
        for _ in range(eng_count):
            ing, eng_amount, measure = file.readline().strip().split(' | ')
            ingridients.append({
                "ingredient_name": ing,
                "quantity": eng_amount,
                "measure": measure

            })
        file.readline()
        recipes[recipe_name] = ingridients
    pprint(recipes, sort_dicts = False)