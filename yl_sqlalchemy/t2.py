from flask import Flask, render_template, redirect
from form.user import RegisterForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/register")
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.email = form.email.data
        user.age = int(form.age.data)
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    return 'Страница пользователя'


if __name__ == '__main__':
    app.run()
