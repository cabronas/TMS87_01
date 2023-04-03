"""
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""


def main():
    a, b, c, d, e = [],[],[],[],[]
    text_file = open('test.txt')
    text_lines = []
    s1 = 1
    s2 = 3
    i = 0
    while True:
        line = text_file.readline()
        #a
        if i == 0:
            a.append(line)
        #b
        if i == 4:
            b.append(line)
        #c
        if i < 4:
            c.append(line)
        #d
        if s1 <= i <= s2:
            d.append(line)
        #e
        e.append(line)
        i += 1
        if not line:
            break
    text_file.close()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == "__main__":
    main()
