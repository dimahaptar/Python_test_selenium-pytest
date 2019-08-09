from .. import selenium_library
from .. import config


def test_contact_us():
    assert selenium_library.contact_us() == config.contact_us

