"""
В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.
"""
inp=input()
result=inp.split(' ')
result.reverse()
print(*result)