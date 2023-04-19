"""
Имеется текстовый файл.
Переписать в другой файл все его
строки с заменой в них символа 0 на символ 1 и наоборот.
"""


def main():
    text_lines = []
    with open('test_new.txt', "r") as read_file:
        with open('test_new1.txt', "w") as write_file:
            rlines = read_file.readlines()
            for rline in rlines:
                wline = ""
                for character in rline:
                    if character == "1":
                        wline += "0"
                    elif character == "0":
                        wline += "1"
                    else:
                        wline += character
                write_file.write(wline)


if __name__ == "__main__":
    main()
