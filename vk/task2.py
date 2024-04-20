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
    response = vk.friends.get(fields="bdate")
    if response['items']:
        for item in sorted(response['items'], key=lambda value: (value['last_name'], value['first_name'])):
            if item.get('first_name', '') != 'DELETED':
                print(item.get('last_name', ''), item.get('first_name', ''), item.get('bdate', ''))


if __name__ == '__main__':
    main()
