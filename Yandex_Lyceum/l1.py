from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def _index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def countdown():
    countdown_list = []
    countdown_list.append('Человечество вырастает из детства.')
    countdown_list.append('Человечеству мала одна планета.')
    countdown_list.append('Мы сделаем обитаемыми безжизненные пока планеты.')
    countdown_list.append('И начнем с Марса!')
    countdown_list.append('Присоединяйся!')
    return '<br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
  <h1 style='color:red'>Жди нас, Марс!</h1>
  <img src="https://sun1-90.userapi.com/T7dgmiPpJDCKD6cCCCiB8YPrnMwMpue6SO1Exg/4o2VuUWxLHQ.jpg" alt="image_mars">
  <p>Вот она такая, красная планета</p>
</body>
</html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/mars.css')}">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
          integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
            integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
            crossorigin="anonymous"></script>
</head> 
<body>
        <h1 style='color: red'>Жди нас, Марс!</h1>
        <img src="{url_for("static", filename="img/img_mars.webp")}"
        alt="Фото Марса украл НЛО"
        height=500 width=500>
        <div class="alert alert-primary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-danger" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-warning" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-dark" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-success" role="alert">
            Присоединяйся!
        </div>
    </body>

</html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Варианты выбора</title>
</head>
<body>
<h1>Мое предложение: {planet_name}</h1>
<div class="alert alert-first" role="alert">
    Эта планета близка к Земле;
</div>
<div class="alert alert-success" role="alert">
    На ней много необходимых ресурсов;
</div>
<div class="alert alert-secondary" role="alert">
    На ней есть вода и атмосфера;
</div>
<div class="alert alert-warning" role="alert">
    На ней есть небольшое магнитное поле;
</div>
<div class="alert alert-danger" role="alert">
    Наконец, она просто красива!
</div>
</body>
</html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                  crossorigin="anonymous">
            <title>Результаты отбора</title>
        </head>
        <body>
        <h1>Результаты отбора</h1>
        <h1>Претендента на участие в миссии{nickname}</h1>
        <div class="alert alert-success" role="alert">
            Поздравляем! Ваш рейтинг после {str(level)} этапа отбора
        </div>
        <div class="alert alert-secondary" role="alert">
             Составляет {str(rating)}!
        </div>
        <div class="alert alert-warning" role="alert">
            Желаем удачи!
        </div>

        </body>
        </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}">
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <title>Результаты отбора</title>
                </head>
                <body>
                <h1 class="text-center">Анкета претендента</h1>
                <h3 class="text-center"> на участие в миссии</h3>
                <div>
                    <form class="login_form" method="post" id="form">
                        <input type="text" placeholder="Введите фамилию" class="form-control" name="firstname">
                        <input type="text" placeholder="Введите имя" class="form-control" name="name"><br>
                        <input type="email" placeholder="Введите e-mail" class="form-control" name="email">
                        <div class="form-group">
                            <label for="classSelect">Какое у вас образование?</label>
                            <select class="form-control" id="classSelect" name="class">
                                <option>Начальное</option>
                                <option>Среднее общее</option>
                                <option>Среднее профессиональное</option>
                                <option>Высшее I степени</option>
                                <option>Высшее II степени</option>
                                <option>Высшее III степени</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Какие у вас есть профессии?</label>
                            <div class="form-check">
                                <input type="checkbox" name="job" id="job" class="form-check-input">
                                <label class="form-check-label" for="job">Инженер-исследователь</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job2">
                                <label class="form-check-label" for="job2">
                                    Инженер-строитель
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job3">
                                <label class="form-check-label" for="job3">
                                    Пилот
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job4">
                                <label class="form-check-label" for="job4">
                                    Метеоролог
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job5">
                                <label class="form-check-label" for="job5">
                                    Инженер по жизнеобеспечению
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job6">
                                <label class="form-check-label" for="job6">
                                    Инженер по радиационной защите
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job7">
                                <label class="form-check-label" for="job7">
                                    Врач
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="sex" id="job8">
                                <label class="form-check-label" for="job8">
                                    Экзобиолог
                                </label>
                            </div>
                        </div>
                        <br>
                        <div class="form-group">
                            <label>Укажите пол</label><br>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" id='male' name="male">
                                <label class="form-check-label" for="male">Мужской</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" id='female' name="male">
                                <label class="form-check-label" for="female">Женский</label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="about">Почему вы хотите участвовать в миссии?</label>
                            <textarea class="form-control" rows="3" name="about" id="about"></textarea>
                        </div>
                        <br>
                        <div class="form-group">
                            <div>
                                <label for="photo">Приложите фотографию</label><br>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                        </div><br>
                        <div class="form-group">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="finish" name="finish" >
                                <label class="form-check-label" for="finish">Готовы остаться на Марсе?</label>
                            </div>
                        </div><br>
                        <div class="form-group">
                            <input type="submit" value="Отправить" class="btn btn-primary">
                        </div>
                    </form>
                </div>
                </body>
            </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run()
