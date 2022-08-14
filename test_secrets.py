import os


class my_secrets:

    login1 = os.getenv("A_USER_LOGIN")
    login2 = os.getenv("A_USER_P")

def test_env():
    assert len(my_secrets.login1) != 0
    assert len(my_secrets.login1) == len("qwertyuiop")
    assert len(my_secrets.login2) == 9
