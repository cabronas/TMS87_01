"""
Создать шаблон flask_06_form.html с формой Имя,
фамилия, возраст.
Создать вью /form: при GET запросе отображать форму,
при POST запросе Выводить данные пользователю с помощью шаблона flask_06_display.html
"""
from flask import *

app = Flask(__name__, template_folder="templates")


@app.route('/enter/', methods=['POST', 'GET'])
def enter():
    if request.method == 'POST':
        # user, lname, age = request.form['name'], request.form['lname'], request.form['age']
        form1 = request.form
        return render_template("flask_06_display.html", user_data = form1)
    else:
        print(app.template_folder)
        return render_template("flask_06_form.html")


if __name__ == '__main__':
    app.run()