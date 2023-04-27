"""
Создать скрипт, который принимает имя папки и создает ее рядом со скриптом
"""
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-fn', required=True)
args = parser.parse_args()
os.mkdir(args.fn)
