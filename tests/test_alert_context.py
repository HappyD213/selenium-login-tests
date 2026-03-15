from pages.alerts_context_page import AlertContextPage
from utils.config_reader import ConfigReader

config = ConfigReader()


def test_alert_context_click(browser):
    browser.get(config.get("DEFAULT", "context_alerts_url"))

    alert_context = AlertContextPage(browser)
    alert_context.wait_for_displayed()

    alert_context.go_to_and_click_element()
    actual_text = alert_context.get_alert_text()
    expected_text = "You selected a context menu"
    assert expected_text in actual_text, (f"Expected text not in actual text\n"
                                          f"Actual text: {actual_text}\n"
                                          f"Expected text: {expected_text}")

    alert_context.accept_alert()
    alert_context.wait_for_alert_closed()
