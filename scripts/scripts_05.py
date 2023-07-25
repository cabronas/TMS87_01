"""
Создать скрипт.
Программа принимает имя папки и имя файла с расширением.
Создает папку и создает в ней файл. Если расширение файла py - записывает в файл следующее:
def main():
    pass
if __name__ == '__main__':
    main()

"""
import sys
import argparse
import os

python_file_text = '''
def main():
    pass
if __name__ == '__main__':
    main()
'''
parser = argparse.ArgumentParser()
parser.add_argument('-fn', required=True)
parser.add_argument('-fin', required=True)
parser.add_argument('-ext', required=True)
args = parser.parse_args()
filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.fn, args.fin)+ "." + args.ext
os.mkdir(args.fn)
f1 = open(filepath, 'w')
if args.ext == "py":
    f1.write(python_file_text)
f1.close()
