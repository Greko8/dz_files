from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for i in range(ing_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients

    # pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book.keys():
            crr = {}
            for ingredients in cook_book[dish]:
                # print(ingredients)
                crr.update(measure=ingredients.get('measure'), quantity = int(ingredients.get('quantity'))*person_count)
                # print(crr)
                result[ingredients.get('ingredient_name')]=crr
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

files_list = ['1.txt', '2.txt', '3.txt']
all = {}

for file_name in files_list:
    with open(file_name, 'rt', encoding='utf-8') as file:
        list = []
        lines = file.readlines()
        list.append(file_name)
        list.append(lines)
        all[len(lines)] = list
        sorted_all = dict(sorted(all.items()))

with open('new_file.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted_all.items():
        file.write(f'{value[0]}\n')
        file.write(f'{key}\n')
        file.writelines(value[1])
        file.write('\n')

pprint(sorted_all, sort_dicts=False)
