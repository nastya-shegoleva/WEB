import vk_api
import datetime


def main():
    login, password = LOGIN, PASSWORD

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5, offset=0)
    if response['items']:
        for i in response['items']:
            text = i['text']
            data = int(i['data'])
            full_date = datetime.datetime.fromtimestamp(data)
            print(text + ';')
            print(f'date: {full_date.date()}, time: {full_date.time()}')


if __name__ == '__main__':
    main()
