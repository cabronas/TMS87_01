"""
Написать скрипт - таймер. Создать программу Pomodoro.

На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут),
длину перерыва(по-умолчанию 5 минут), количество циклов(по-умолчанию 4) и название задачи.
Программа указывает оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки.
Программа должна вести файл лога о всех запусках.
"""

import os
from datetime import *
import argparse
import time
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-fn', required=True)
parser.add_argument('-ln', required=True)
parser.add_argument('-m', type=int, default=25, required=True)
parser.add_argument('-br', type=int, default=5, required=True)
parser.add_argument('-cc', type=int, default=4, required=True)
parser.add_argument('-tname', required=True)
args = parser.parse_args()

start_time = datetime.now()
with open('log.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    fields = ['first name', 'last name', 'time start', 'task name']
    csvwriter.writerow(fields)
    arr = [args.fn, args.ln, start_time, args.tname]
    csvwriter.writerow(arr)


def cycle(state, time_to):
    delta_time = timedelta(minutes=time_to)
    print(f'start {state}')
    while delta_time > timedelta():  # 0:00:00
        print(f'Remaining time - {delta_time}')
        delta_time -= timedelta(minutes=1)
        time.sleep(60)
    print(f'end of {state}')


for i in range(0, args.cc):
    print(f'cycle - {i + 1}')
    cycle('focus', args.m)
    cycle('break', args.br)
