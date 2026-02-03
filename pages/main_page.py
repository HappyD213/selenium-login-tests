from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.search_page import SearchPage


class MainPage(BasePage):
    URL = "https://store.steampowered.com/"

    MAIN_PAGE_UNIQUE = (By.XPATH, "//h2[@id='home_featured_and_recommended']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global_action_link') and contains(@href, 'login')]")
    GAME_SEARCH_INPUT = (By.XPATH, "//form[@role='search']//input[@type='text']")
    GAME_SEARCH_BUTTON = (By.XPATH, "//form[@role='search']//button[@type='submit']")

    def open_main_page(self):
        self.open(self.URL)
        self.wait_for_visible(self.MAIN_PAGE_UNIQUE)
        self.wait_for_ready_state()

    def search_game(self, game_name):
        self.type(self.GAME_SEARCH_INPUT, game_name)
        self.click(self.GAME_SEARCH_BUTTON)
        return SearchPage(self.browser)

    def type_in_game_search_input(self, game_name):
        self.type(self.GAME_SEARCH_INPUT, game_name)
