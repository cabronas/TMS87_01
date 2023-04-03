"""
Имеются два текстовых файла с одинаковым числом строк.
Выяснить, совпадают ли их строки.
Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.
"""


def main():
    file1 = open('test.txt')
    file2 = open('test3.txt')
    while line1 := file1.readline():
        line2 = file2.readline()
        if line1 != line2:
            print(line1, line2)
            break
    file1.close()
    file2.close()


if __name__ == "__main__":
    main()
