from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    GAME_SEARCH_INPUT = (By.XPATH, "//form[@role='search']//input[@type='text']")
    GAME_SEARCH_BUTTON = (By.XPATH, "//form[@role='search']//button[@type='submit']")
    SEARCH_PAGE_UNIQUE = (By.XPATH, "//div[@id='search_result_container']")
    SORT_DROPDOWN = (By.XPATH, "//button[@id='sort_by_trigger']")
    SORT_OPTION_PRICE_DESC = (By.XPATH, "//a[@id='Price_DESC']")
    SEARCH_RESULTS_CONTAINER = (By.XPATH, "//div[@id='search_resultsRows']")
    SEARCH_ITEMS = (By.XPATH, "//div[@id='search_resultsRows']/a[contains(@class, 'search_result_row')]")

    def search_page_is_displayed(self):
        self.wait_for_visible(self.SEARCH_PAGE_UNIQUE)
        self.wait_for_ready_state()

    def type_game_name(self, game_name):
        self.type(self.GAME_SEARCH_INPUT, game_name)

    def sort_price_by_desc(self):
        self.click(self.SORT_DROPDOWN)
        self.click(self.SORT_OPTION_PRICE_DESC)

    def get_games_list(self, n):
        self.wait_for_n_elements(self.SEARCH_RESULTS_CONTAINER, self.SEARCH_ITEMS, n)

