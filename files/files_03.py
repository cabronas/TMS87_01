"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""


def main():
    text_lines = []
    with open('test_new.txt', "a") as text_file:
        for i in range(3):
            inline = input(f"{i} line - ")
            text_lines.append((inline + "\n"))
        text_file.writelines(text_lines)


if __name__ == "__main__":
    main()
