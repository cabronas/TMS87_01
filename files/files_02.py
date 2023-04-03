"""
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры.
"""


def main():
    text_lines = []
    with open('test_new.txt', "w") as text_file:
        for i in range(6):
            inline = input(f"{i} line - ")
            text_lines.append((inline+"\n"))
        text_file.writelines(text_lines)


if __name__ == "__main__":
    main()
