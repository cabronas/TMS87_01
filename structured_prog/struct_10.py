"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы получить список ключей - использовать метод .keys()

(подсказка: создается новый ключ с цифрой в конце, старый удаляется)

предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.

"""
# for
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key, value in list(d.items()):
    s = key + str(len(key))
    d.update({s: value})
    d.pop(key)
print(d)

# while
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keyList = list(d.keys())
counter = 0
while counter != len(keyList):
    s = keyList[counter] + str(len(keyList[counter]))
    d.update({s: d[keyList[counter]]})
    d.pop(keyList[counter])
    counter += 1
print(d)
