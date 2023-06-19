import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def HW():
    return str(datetime.datetime.now())


if __name__ == '__main__':
    app.run()
