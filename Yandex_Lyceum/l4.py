from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def start():
    return ''


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    engineer = any(map(lambda engr: engr in prof, ("инженер", "строитель")))
    return render_template('prof.html', engineer=engineer)


@app.route('/distribution')
def distribution():
    lst_cosmonavt = ["Ридли Скотт", "Энди Уир", "Шон Бин"]
    return render_template('distribution.html', cosmonavt_list=lst_cosmonavt)


@app.route('/table/<string:gender>/<int:age>')
def color_kaute(gender, age):
    return render_template('color_kaute.html', gender=gender, age=age)


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


class LoginForm(FlaskForm):
    id_astronaut = StringField('id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return f'''<h1>Доступ разрешен</h1>'''


@app.route('/member')
def member():
    with open("templates/personal_card.json", "rt", encoding="utf8") as f:
        member_list = json.loads(f.read())
    return render_template('personal_card.html', member=member_list)


if __name__ == '__main__':
    app.run()
