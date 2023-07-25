"""
Создать скрипт.
Программа принимает имя папки и имя файла. Создает папку и создает в ней файл
"""
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-fn', required=True)
parser.add_argument('-fin', required=True)
args = parser.parse_args()
sourcepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.fn, args.fin)
os.mkdir(args.fn)
f1 = open(sourcepath, 'w')
f1.close()
