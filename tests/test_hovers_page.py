import pytest
from pages.hovers_page import HoversPage
from utils.config_reader import ConfigReader

config = ConfigReader()


@pytest.mark.parametrize("index, expected_name",
                         [
                             (0, "name: user1"),
                             (1, "name: user2"),
                             (2, "name: user3"),

                         ])
def test_hovers_page(browser, index, expected_name):
    browser.get(config.get("DEFAULT", "hovers_url"))
    hovers_page = HoversPage(browser)
    hovers_page.wait_for_displayed()
    hovers_page.move_to_user(index)

    actual_user_name = hovers_page.wait_user_name_visible(index)
    expected_user_name = expected_name
    assert expected_user_name == actual_user_name, (f"Actual name not equal to expected name\n"
                                                    f"Actual name: {actual_user_name}\n"
                                                    f"Expected name: {expected_user_name}")
