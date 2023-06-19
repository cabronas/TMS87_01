"""
Создать шаблон с формой Имя, фамилия, возраст. Передать данные на вью дописать эти данные в файл
"""
import datetime

from flask import Flask

from flask import *

app = Flask(__name__)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user, lname, age = request.form['name'], request.form['lname'], request.form['age']
        return redirect(url_for('enter', name=user, lname=lname, age=age))
    else:
        ar = request.args.to_dict()
        user, lname, age = ar['name'], ar['lname'], ar['age']
        return redirect(url_for('enter', name=user, lname=lname, age=age))


@app.route('/success/<name><lname><age>')
def enter(name, lname, age):
    with open("test_04.txt", "w") as file1:
        file1.writelines([name, lname, age])
    return str(name + lname + age)


if __name__ == '__main__':
    app.run()
