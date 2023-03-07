"""
Создать список произвольного содержания. После каждой операции выводить список на экран
Добавить к нему строку “Hello”.
Удалить первый элемент.
Поменять второй элемент на строку “World”.
Удалить элемент “World”
Вывести на экран перевернутый список
"""
list = [0, 1, 2]
print(list)
list.append("Hello")
print(list)
list.pop(0)
print(list)
list[1] = "World"
print(list)
list.remove("World")
print(list)
list.reverse()
print(list)
