# phone_book = {'Ruslan': [89870946842, 55646568], 'Ruslan2': 89613664866}
# print(phone_book['Ruslan'])
# phone_book['Alsu'] = 89273756342
# del phone_book['Ruslan']  удаление
# phone_book.update({'Sahsa': 1256156155,
#                    'Alex': 15466545})
#print(phone_book)
# print(phone_book.get('Eldar', 'Такого ключа нет!'))
#a = phone_book.pop('Alsu')
#list_ = [1, 2, 3]
#list_.pop(0)
#print(list_)
#print(phone_book)
#print(a)
#print(phone_book.keys())
#print(phone_book.values())
#print(phone_book.items())
# print(phone_book)
# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1,2,3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# list_ = set(list_)
# print(list_)
# # print(list_.discard(1))
# print(list_.add(5))
# print(list_)
Dict = {'Ruslan': 1993, 'Alsu': 2000, 'Malika': 2021}
print(Dict)
print(Dict['Alsu'])
print(Dict.get('Eldar'))
Dict.update({'Tany': 1975, 'Malik': 2022})
print(Dict)
a = Dict.pop('Ruslan')
print(Dict)
print(a)
my_set = {1, 2, 'Auto', 2, 1, 1, 2, 3.14}
print(my_set)
set_ = [1, 1, 1, 2, 3, 1, 2, 3, 1]
set_ = set(my_set)
print(my_set.update([5, 7]))
print(my_set)
print(set_.discard(1))
print(set_)