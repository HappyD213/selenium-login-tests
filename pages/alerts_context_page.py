from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import document_ready, is_alert_closed
from selenium.webdriver.common.action_chains import ActionChains


class AlertContextPage(BasePage):
    ALERT_CONTEXT_UNIQUE = (By.ID, "hot-spot")

    def wait_for_displayed(self):
        self.wait.until(EC.element_to_be_clickable(self.ALERT_CONTEXT_UNIQUE))
        self.wait.until(document_ready())

    def go_to_and_click_element(self):
        element = self.wait.until(EC.visibility_of_element_located(self.ALERT_CONTEXT_UNIQUE))
        ActionChains(self.driver) \
            .move_to_element(element) \
            .context_click() \
            .perform()

    def wait_for_alert_closed(self):
        self.wait.until(lambda d: is_alert_closed(d))

    def get_alert_text(self):
        text = self.wait.until(lambda d: d.switch_to.alert).text
        return text

    def accept_alert(self):
        self.wait.until(lambda d: d.switch_to.alert).accept()