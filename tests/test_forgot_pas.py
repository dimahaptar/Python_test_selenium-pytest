from .. import selenium_library
from .. import config


def test_forgot_pass():
    assert selenium_library.forgot_pas() == config.forgot_pas