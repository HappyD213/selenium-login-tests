import pytest
from pages.hovers_page import HoversPage
from config.config_reader import ConfigReader

config = ConfigReader()


@pytest.mark.parametrize("index, expected_name",
                         [
                             (1, "name: user1"),
                             (2, "name: user2"),
                             (3, "name: user3"),

                         ])
def test_hovers_page(browser, index, expected_name):
    browser.get(ConfigReader.get_hovers_url())
    hovers_page = HoversPage(browser)
    hovers_page.wait_for_open()

    expected_user_name = expected_name
    actual_user_name = hovers_page.get_n_user_name(index)
    assert expected_user_name == actual_user_name, f"Expected not equal to Actual: {repr(expected_user_name)} != {repr(actual_user_name)}"
