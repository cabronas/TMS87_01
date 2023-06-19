"""
Создать сайт. При запросе по урлу /my_word/[word],
в случае если длина слова четна - выводит строку содержащую все нечетные элементы строки(abcdef -> ace).
В ином случае перенаправлять на домашнюю страницу.
"""
import datetime

from flask import Flask

from flask import *

app = Flask(__name__)


@app.route('/my_world/<word>/')
def HW(word):
    print(len(word))
    if len(word) % 2 != 0:
        return redirect(url_for('HW1'))
    else:
        return word[::2]


@app.route('/a/')
def HW1():
    return 'hello'


if __name__ == '__main__':
    app.run()
