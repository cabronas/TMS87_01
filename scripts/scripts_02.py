"""
Создать скрипт, который принимает имя фамилию и возраст и дописывает их в файл
"""
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', required=True)
parser.add_argument('-ln', required=True)
parser.add_argument('-ag', required=True)
args = parser.parse_args()
with open("file1.txt", 'w') as file:
    file.write(f"{args.fn} {args.ln} {args.ag}")
