"""
Создать словарь произвольного содержания. После каждой операции выводить словарь на экран
Добавить новую пару по ключу alex. Значение - 42
Вывести на экран значение по ключу alex.
Изменить значение по ключу alex на 55.
Удалить элемент с ключом alex.
"""
dict = {'a': 1, 'b': 2}
print(dict)
dict['alex'] = 42
print(dict)
print(dict['alex'])
dict['alex'] = 55
print(dict)
dict.pop('alex')
print(dict)
