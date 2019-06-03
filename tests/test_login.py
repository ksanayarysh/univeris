def test_1(open_login_page, get_user_name, get_password):
    open_login_page.login(get_user_name, get_password)


def test_cred(get_url, get_user_name, get_password):
    print(get_url, get_user_name, get_password)
    print(type(get_url))