# from users import User
# from db_session import global_init, create_session

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    db_sess = create_session()
    for user in db_sess.query(User).all():
        if user.address == 'module_1' and user.age < 21:
            user.address = 'module_3'
    db_sess.commit()


if __name__ == '__main__':
    main()
