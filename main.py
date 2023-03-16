from pprint import pprint
with open('recipes.txt', 'r', encoding="utf-8") as file:
    cook_book = {}
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
        cook_book[recipe_name] = ingridients
    #pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    shopping = {}
    for dish, ingridients in cook_book.items():
        if dish in dishes:
            for ingridient in ingridients:
                name = ingridient["ingredient_name"]
                quantity = int(ingridient["quantity"]) * person_count
                measure = ingridient["measure"]
                if name not in shopping.keys():
                    shopping[name] = {
                        "measure": measure,
                        "quantity": quantity
                    }
                else:
                    shopping[name]["quantity"] += quantity
    return shopping


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет', "Запеченный картофель с курицей", "Запеченный картофель"], 1))