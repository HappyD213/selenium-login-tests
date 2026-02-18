from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.parsers import get_prices
from utils.waits import DocumentReady
from utils.parsers import get_prices
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    GAME_SEARCH_INPUT = (By.XPATH, "//form[@role='search']//input[@type='text']")
    GAME_SEARCH_BUTTON = (By.XPATH, "//form[@role='search']//button[@type='submit']")
    SEARCH_PAGE_UNIQUE = (By.ID, "search_result_container")
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_OPTION_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULTS_CONTAINER = (By.ID, "search_resultsRows")
    SEARCH_ITEMS = (By.XPATH, "//*[@id='search_resultsRows']/a[contains(@class, 'search_result_row')]")
    LOADER = (By.XPATH, "//div[contains(@style,'opacity: 0.5')]")

    DISCOUNT_PRICE_ELEMENT = (By.XPATH, "//a//div[contains(@class, 'search_price_discount_combined')]")

    def wait_for_opening(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_PAGE_UNIQUE))
        self.wait.until(DocumentReady())

    def sort_price_by_desc(self, n):
        self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SORT_OPTION_PRICE_DESC)).click()
        self.fast_wait.until(EC.visibility_of_element_located(self.LOADER))
        self.fast_wait.until_not(EC.visibility_of_element_located(self.LOADER))

    def get_prices(self, n):
        return self.wait.until(get_prices(self.DISCOUNT_PRICE_ELEMENT, n))
