import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def HW(number):
    return str(number * number)


if __name__ == '__main__':
    app.run()
