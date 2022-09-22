import pytest


def always_returns_true():
    x = 3 + 4
    return x


def test_always_returns_true():
    assert always_returns_true()
