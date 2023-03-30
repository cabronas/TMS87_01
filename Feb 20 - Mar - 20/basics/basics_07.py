"""
Ввести предложение состоящее из двух слов. Поменять местами слова, добавить восклицательный знак в начало и конец, вывести итоговое предложение на экран.
"""
inString = input()
outList = inString.split(' ')
outList.reverse()
outList.insert(0, '!')
outList.insert(len(outList), '!')
print(*outList)
