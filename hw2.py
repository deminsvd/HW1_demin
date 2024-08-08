cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    i = 0
    while i!=2:
        index = f.readline().strip()
        if index != '':
            i=0
            recipe = []
            for ingred_index in range(int(f.readline().strip())):
                ingredient_list = f.readline().strip().split(' | ')
                ingredient = {}
                ingredient['ingredient_name'] = ingredient_list[0]
                ingredient['quantity'] = ingredient_list[1]
                ingredient['measure'] = ingredient_list[2]
                recipe.append(ingredient)
            cook_book[index] = recipe
        else:
            i+=1
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list[ingredient['ingredient_name']] = {'measure':ingredient['measure'],'quantity':int(ingredient['quantity'])*person_count}
    print(shop_list)

print(cook_book)
print()

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)