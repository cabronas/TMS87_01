"""
Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл
"""
from random import randint
import json


def main():
    mat = [[randint(0, 5) for j in range(3)]
           for i in range(3)]
    with open("json1.txt", "w") as file1:
        data = json.dumps(mat)
        file1.write(data)
    with open("json1.txt") as file1:
        data = json.loads(file1.read())
        # print(data, type(data))
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] % 2 == 0:
                    data[i][j] = 0
    with open("json2.txt", "w") as file1:
        data = json.dumps(data)
        file1.write(data)


if __name__ == "__main__":
    main()
