from browser.browser import Browser
from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage
from faker import Faker

fake = Faker()


class AlertsPage(BasePage):
    JS_ALERT_LOC = "//*[contains(@onclick, 'jsAlert()')]"
    JS_CONFIRM_LOC = "//*[contains(@onclick, 'jsConfirm()')]"
    JS_PROMPT_LOC = "//*[contains(@onclick, 'jsPrompt()')]"
    RESULT_LOC = "result"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Alerts Page"

        self.unique_element = Button(self.browser, self.JS_ALERT_LOC, description="Alerts page -> Unique element")

        self.js_alert_button = Button(self.browser, self.JS_ALERT_LOC, description="Alerts page -> Js alert button")
        self.js_confirm_button = Button(self.browser, self.JS_CONFIRM_LOC,
                                        description="Alerts page -> Js confirm button")
        self.js_prompt_button = Button(self.browser, self.JS_PROMPT_LOC, description="Alerts page -> Js prompt button")
        self.result_element = WebElement(self.browser, self.RESULT_LOC, description="Alerts page -> Result element")

    def alert_button_click(self):
        self.js_alert_button.click()
        self.browser.wait_alert_present()

    def confirm_button_click(self):
        self.js_confirm_button.click()
        self.browser.wait_alert_present()

    def prompt_button_click(self):
        self.js_prompt_button.click()
        self.browser.wait_alert_present()

    def js_alert_button_click(self):
        self.js_alert_button.js_click()
        self.browser.wait_alert_present()

    def js_confirm_button_click(self):
        self.js_confirm_button.js_click()
        self.browser.wait_alert_present()

    def js_prompt_button_click(self):
        self.js_prompt_button.js_click()
        self.browser.wait_alert_present()

    def get_result_text(self):
        return self.result_element.get_text()
