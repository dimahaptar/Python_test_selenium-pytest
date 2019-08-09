from .. import selenium_library
from .. import config


def test_creare_acc():
    assert selenium_library.create_acc() == config.create_acc

