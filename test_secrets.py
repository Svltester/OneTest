import os


class my_secrets:
    login = os.environ['A_USER_LOGIN']


def test_env():
    assert len(my_secrets.login) != 0
    assert len(my_secrets.login) == len("qwertyuiop")
