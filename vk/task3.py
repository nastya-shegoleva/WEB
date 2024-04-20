import vk_api

GROUP_ID = YOUR_ID
ALBUM_ID = YOUR_ID


def main():
    login, password = LOGIN, PASSWORD

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    # vk = vk_session.get_api()
    upload.photo(photos=['static/img/me.jpg', 'static/img/дремучий лес.jpg', 'static/img/темный лес.jpg'],
                 album_id=ALBUM_ID,
                 group_id=GROUP_ID)


if __name__ == '__main__':
    main()
