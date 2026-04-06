import faker
from pages.alerts_page import AlertsPage
from config.config_reader import ConfigReader

config = ConfigReader()
fake = faker.Faker()


def test_alerts(browser):
    browser.get(config.get("DEFAULT", "alerts_url"))
    alerts_page = AlertsPage(browser)
    alerts_page.wait_for_open()

    # JS ALERT
    alerts_page.js_alert_button_click()
    actual_alert_text = browser.get_alert_text()
    expected_alert_text = "I am a JS Alert"
    assert expected_alert_text == actual_alert_text, f"Expected: {expected_alert_text} Actual: {actual_alert_text}"

    browser.accept_alert()
    browser.wait_alert_gone()
    actual_result_text = alerts_page.get_result_text()
    expected_result_text = "You successfully clicked an alert"
    assert expected_result_text == actual_result_text, f"Expected: {expected_result_text} Actual: {actual_result_text}"

    # JS CONFIRM
    alerts_page.js_confirm_button_click()
    actual_alert_text = browser.get_alert_text()
    expected_alert_text = "I am a JS Confirm"
    assert expected_alert_text in actual_alert_text, f"Expected: {expected_alert_text} Actual: {actual_alert_text}"

    browser.accept_alert()
    browser.wait_alert_gone()
    actual_result_text = alerts_page.get_result_text()
    expected_result_text = "You clicked: Ok"
    assert expected_result_text in actual_result_text, f"Expected: {expected_result_text} Actual: {actual_result_text}"

    # JS PROMPT
    alerts_page.js_prompt_button_click()
    actual_alert_text = browser.get_alert_text()
    expected_alert_text = "I am a JS prompt"
    assert expected_alert_text in actual_alert_text, f"Expected: {expected_alert_text} Actual: {actual_alert_text}"

    text_for_test = fake.text(10)
    browser.send_keys_alert(text_for_test)
    browser.accept_alert()
    browser.wait_alert_gone()
    actual_result_text = alerts_page.get_result_text()
    expected_result_text = f"You entered: {text_for_test}"
    assert expected_result_text in actual_result_text, f"Expected: {expected_result_text} Actual: {actual_result_text}"
