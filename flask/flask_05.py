"""
Создать папку templates в корне проекта. Создать шаблон flask_05.html с формой Имя, фамилия, возраст.
Создать вью /form: при GET запросе отображать форму, при POST запросе дописывать переданные данные в файл.
"""

from flask import Flask

from flask import *

app = Flask(__name__, template_folder=" templates")


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user, lname, age = request.form['name'], request.form['lname'], request.form['age']
        return redirect(url_for('enter', name=user, lname=lname, age=age))
    else:
        print(app.template_folder)
        return render_template("form_04.html")


@app.route('/success/<name><lname><age>')
def enter(name, lname, age):
    with open("test_04.txt", "w") as file1:
        file1.writelines([name, lname, age])
    return str(name + lname + age)


if __name__ == '__main__':
    app.run()