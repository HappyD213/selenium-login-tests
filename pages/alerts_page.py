from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import document_ready

class AlertsPage(BasePage):
    JS_ALERT = (By.XPATH, "//*[contains(@onclick, 'jsAlert()')]")
    JS_CONFIRM = (By.XPATH, "//*[contains(@onclick, 'jsConfirm()')]")
    JS_PROMPT = (By.XPATH, "//*[contains(@onclick, 'jsPrompt()')]")
    RESULT = (By.ID, "result")

    def wait_for_opening(self):
        self.wait.until(EC.visibility_of_element_located(self.JS_ALERT))
        self.wait.until(document_ready())

    def click_js_alert_button(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_ALERT)).click()

    def click_js_confirm_button(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_CONFIRM)).click()

    def click_js_prompt_button(self):
        self.wait.until(EC.element_to_be_clickable(self.JS_PROMPT)).click()

    def get_js_alert_text(self):
        text = self.wait.until(lambda d: d.switch_to.alert).text
        return text

    def alert_accept(self):
        self.wait.until(lambda d: d.switch_to.alert).accept()

    def get_actual_result_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.RESULT)).text

    def alert_send_keys(self, text):
        self.wait.until(lambda d: d.switch_to.alert).send_keys(text)