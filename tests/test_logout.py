from .. import selenium_library
from .. import config


def test_logout():
    assert selenium_library.logout() == config.logout


