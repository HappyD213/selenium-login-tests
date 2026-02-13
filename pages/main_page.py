from selenium.webdriver.common.by import By
from utils.waits import DocumentReady
from pages.base_page import BasePage
from pages.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    MAIN_PAGE_UNIQUE = (By.ID, "home_featured_and_recommended")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global_action_link') and contains(@href, 'login')]")
    GAME_SEARCH_INPUT = (By.XPATH, "//form[@role='search']//input[@type='text']")
    GAME_SEARCH_BUTTON = (By.XPATH, "//form[@role='search']//button[@type='submit']")

    def is_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.MAIN_PAGE_UNIQUE))
        self.wait.until(DocumentReady())

    def search_game(self, game_name):
        self.wait.until(EC.visibility_of_element_located(self.GAME_SEARCH_INPUT)).send_keys(game_name)
        self.wait.until(EC.element_to_be_clickable(self.GAME_SEARCH_BUTTON)).click()
