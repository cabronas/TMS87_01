"""
Написать скрипт - таймер.
Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
После программа начинает обратный отсчет выводя оставшееся время.
Программа должна хранить файл логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!
"""
import time
from datetime import *
import sys
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('-ho', required=True)
parser.add_argument('-mi', required=True)
parser.add_argument('-se', required=True)
args = parser.parse_args()
start_time = datetime.now()

with open("log.txt", 'w') as log:
    log.writelines([start_time.strftime("%H:%M:%S"), '\n', os.getlogin()])
log.close()

end_time = start_time + timedelta(hours=int(args.ho), minutes=int(args.mi), seconds=int(args.se))
current_time = start_time
while current_time != end_time:
    print(current_time.strftime("%H:%M:%S"))
    current_time += timedelta(seconds=1)
    time.sleep(1)
print("ALARM!!!")
