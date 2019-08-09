from .. import selenium_library
from .. import config


def test_login():
    assert selenium_library.login() == config.username

