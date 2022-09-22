import pytest


def always_returns_true():
<<<<<<< HEAD
    x = 3 + 4
    return x
=======
    return "True"

>>>>>>> 7aab387119de7593008ae3790958ab8c65ef49ff


def test_always_returns_true():
    assert always_returns_true()
