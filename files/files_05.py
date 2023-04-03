"""
Имеется текстовый файл.
Все четные строки этого файла записать во второй файл,
а нечетные — в третий файл. Порядок следования строк сохраняется.
"""


def main():
    file1 = open('test.txt')
    file2 = open('test2.txt', "w")
    file3 = open('test3.txt', "w")
    i = 1
    while line := file1.readline():
        if i % 2 == 0:
            file2.writelines(line)
        else:
            file3.writelines(line)
        i += 1
    file1.close()
    file2.close()
    file3.close()


if __name__ == "__main__":
    main()
