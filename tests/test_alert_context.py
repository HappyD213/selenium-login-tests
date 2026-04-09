from pages.alerts_context_page import AlertContextPage
from config.config_reader import ConfigReader


def test_alert_context_click(browser):
    browser.get(ConfigReader.get_context_alerts_url())

    context_page = AlertContextPage(browser)
    context_page.wait_for_open()

    context_page.right_click_context_menu()
    actual_alert_text = browser.get_alert_text()
    expected_alert_text = "You selected a context menu"
    assert expected_alert_text in actual_alert_text, f"Expected: {expected_alert_text}, Actual: {actual_alert_text}"

    browser.accept_alert()
    browser.wait_alert_gone()
