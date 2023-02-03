
# with open('recipes.txt', 'rt', encoding='utf-8') as file:
#     cook_book = {}
#     for line in file:
#         dish_name = line.strip()
#         number_ingredients = int(file.readline())
#         ingredients = []
#         for num_ingredients in range(number_ingredients):
#             first_ingr = file.readline().strip()
#             name, quantity, measure = first_ingr.split(' | ')
#             ingredients.append({
#                 'name': name,
#                 'quantity': quantity,
#                 'measure': measure
#             })
#         file.readline()
#         cook_book[dish_name] = ingredients

#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    list_ingredients = {}
    for dish_names in dishes:
        if dish_names in cook_book.keys():
            for list_i in cook_book[dish_names]:
                quanity_measure = {}
                if list_i['name'] not in list_ingredients:
                    quanity_measure['quantity'] = int(list_i['quantity'])*person_count
                    quanity_measure['measure'] = list_i['measure']
                    list_ingredients[list_i['name']] = quanity_measure
    return list_ingredients

#print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))

# def open_file(name_file):
#     new_dict = {}
#     dict_text = {}
#     name_txt = name_file
#     result = {}
#     with open (name_file, 'r', encoding='utf-8') as file:
#         len_line = 0
#         text_line = []
#         for line in file:
#             len_line += 1
#             text_line.append(line)
#             new_dict[name_txt] = len_line
#         dict_text.setdefault(name_txt, len_line)
#     sorted_dict = sorted(dict_text, key=dict_text.get)
#     for w in sorted_dict:
#         result[w] = new_dict[w]
#     return result
#
# #print(open_file('1.txt'), open_file('2.txt'), open_file('3.txt'))
#
# def new_file(dict_one):
#     with open('newfile.txt', 'w', encoding='utf-8') as file:
#         for names, numbers in dict_one.items():
#             file.write(names + '\n')
#             file.write(str(numbers) + '\n')
#             with open(names,'r', encoding='utf-8') as f:
#                 res = f.readlines()
#     return res
#
# print(new_file(open_file('1.txt')), new_file(open_file('2.txt')), new_file(open_file('3.txt')))

result_dict = {}

def open_file():
    text_list = ['1.txt', '2.txt', '3.txt']
    new_dict = {}
    for file_name in text_list:
        name_txt = file_name
        with open (file_name, 'r', encoding='utf-8') as file:
            new_dict[name_txt] = len(file.readlines())
    for w in sorted(new_dict, key=new_dict.get):
        print(sorted(new_dict, key=new_dict.get))
        result_dict[w] = new_dict[w]
    return result_dict


def new_file():
            with open('newfile.txt', 'w', encoding='utf-8') as file:
                for names, numbers in open_file().items():
                    with open(names, 'r', encoding='utf-8') as f:
                        file.write(f'{names}\n{numbers}\n{"".join(f.readlines())}\n')

new_file()