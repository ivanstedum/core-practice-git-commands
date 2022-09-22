import pytest


def always_returns_true():
    return bool(1)



def test_always_returns_true():
    assert always_returns_true()
