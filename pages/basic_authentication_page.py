from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import document_ready, element_has_text
from pages.base_page import BasePage


class BasicAuthenticationPage(BasePage):
    BASIC_AUTHENTICATION_UNIQUE = (By.XPATH, "//*[@id='content']//p")

    def wait_for_opening(self):
        self.wait.until(EC.visibility_of_element_located(self.BASIC_AUTHENTICATION_UNIQUE))
        self.wait.until(document_ready())

    def get_element_text(self):
        return self.wait.until(element_has_text(self.BASIC_AUTHENTICATION_UNIQUE))
