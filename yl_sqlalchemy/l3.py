# from users import User
# from db_session import global_init, create_session

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    db_sess = create_session()
    inf_id = db_sess.query(Department).filter(Department.id == 1).first()
    member_inf_id = inf_id.members.split(', ')
    for id_ind in member_inf_id:
        sum_work = 0
        for job in db_sess.query(Job).all():
            if str(id_ind) in job.collaborators:
                sum_work += job.work_size
        if sum_work > 25:
            user = db_sess.query(User).filter(User.id == str(id_ind)).first()
            print(user.surname, user.name)


if __name__ == '__main__':
    main()
