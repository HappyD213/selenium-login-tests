import faker
import pytest
from pages.alerts_page import AlertsPage
from utils.config_reader import ConfigReader

config = ConfigReader()
fake = faker.Faker()


def test_alerts(browser):
    browser.get(config.get("DEFAULT", "alerts_url"))
    alerts_page = AlertsPage(browser)
    alerts_page.wait_for_opening()

    # JS Alert
    alerts_page.click_js_alert_button()
    actual_js_alert_text = alerts_page.get_js_alert_text()
    expected_js_alert_text = "I am a JS Alert"
    assert expected_js_alert_text in actual_js_alert_text, (f"Expected not in actual\n"
                                                            f"Actual: {actual_js_alert_text}\n"
                                                            f"Expected: {expected_js_alert_text}")

    alerts_page.alert_accept()
    expected_result = "You successfully clicked an alert"
    actual_result = alerts_page.get_actual_result_text()
    assert expected_result in actual_result, (f"Expected result not in actual\n"
                                              f"Actual: {actual_result}\n"
                                              f"Expected: {expected_result}")
    # JS Confirm
    alerts_page.click_js_confirm_button()
    expected_js_confirm_text = "I am a JS Confirm"
    actual_js_confirm_text = alerts_page.get_js_alert_text()
    assert expected_js_confirm_text in actual_js_confirm_text, (f"Expected not in actual\n"
                                                                f"Actual: {actual_js_confirm_text}\n"
                                                                f"Expected: {expected_js_confirm_text}")

    alerts_page.alert_accept()
    expected_result = "You clicked: Ok"
    actual_result_confirm = alerts_page.get_actual_result_text()
    assert expected_result in actual_result_confirm, (f"Expected result not in actual\n"
                                                      f"Actual: {actual_result_confirm}\n"
                                                      f"Expected: {expected_result}")

    # JS Prompt
    alerts_page.click_js_prompt_button()
    expected_js_prompt_text = "I am a JS prompt"
    actual_js_prompt_text = alerts_page.get_js_alert_text()
    assert expected_js_prompt_text in actual_js_prompt_text, (f"Expected not in actual\n"
                                                              f"Actual: {actual_js_prompt_text}\n"
                                                              f"Expected: {expected_js_prompt_text}")

    some_random_text = fake.text(max_nb_chars=10)
    expected_result_prompt = f"You entered: {some_random_text}"
    alerts_page.alert_send_keys(some_random_text)
    alerts_page.alert_accept()
    actual_result_prompt = alerts_page.get_actual_result_text()
    assert expected_result_prompt in actual_result_prompt, (f"Expected result not in actual\n"
                                                            f"Actual: {actual_result_prompt}\n"
                                                            f"Expected: {expected_result_prompt}")
