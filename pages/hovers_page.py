from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from utils.waits import document_ready, get_elements, get_users_names


class HoversPage(BasePage):
    HOVERS_PAGE_UNIQUE = (By.XPATH, "(//img[contains(@alt, 'User Avatar')])[1]")
    USER_CONTAINER = (By.XPATH, "//div[contains(@class,'figure')]")
    USER_NAME = (By.XPATH, "//div[contains(@class, 'figcaption')]//h5")

    def wait_for_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.HOVERS_PAGE_UNIQUE))
        self.wait.until(document_ready())

    def move_to_user(self, index):
        users = self.wait.until(get_elements(self.USER_CONTAINER))
        user = users[index]
        ActionChains(self.driver) \
            .move_to_element(user) \
            .perform()

    def wait_user_name_visible(self, index):
        elements = self.wait.until(get_users_names(self.USER_NAME))
        users_names = [element.text for element in elements]
        user_name = users_names[index]
        return user_name
