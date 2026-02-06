from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.waits import DocumentReady, GetPrices, LoaderIsVisible
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    GAME_SEARCH_INPUT = (By.XPATH, "//form[@role='search']//input[@type='text']")
    GAME_SEARCH_BUTTON = (By.XPATH, "//form[@role='search']//button[@type='submit']")
    SEARCH_PAGE_UNIQUE = (By.XPATH, "//*[@id='search_result_container']")
    SORT_DROPDOWN = (By.XPATH, "//*[@id='sort_by_trigger']")
    SORT_OPTION_PRICE_DESC = (By.XPATH, "//*[@id='Price_DESC']")
    SEARCH_RESULTS_CONTAINER = (By.XPATH, "//*[@id='search_resultsRows']")
    SEARCH_ITEMS = (By.XPATH, "//*[@id='search_resultsRows']/a[contains(@class, 'search_result_row')]")
    LOADER_CONTAINER = (By.XPATH, "//*[@id='search_result_container']")
    DISCOUNT_PRICE_ELEMENT = By.XPATH, "//a//div[contains(@class, 'search_price_discount_combined')]"

    def search_page_is_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_PAGE_UNIQUE))
        self.wait.until(DocumentReady())

    def sort_price_by_desc(self, n):
        self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.SORT_OPTION_PRICE_DESC)).click()
        self.wait.until(LoaderIsVisible(self.LOADER_CONTAINER))
        self.wait.until_not(LoaderIsVisible(self.LOADER_CONTAINER))

    def get_prices(self, n):
        return self.wait.until(GetPrices(self.DISCOUNT_PRICE_ELEMENT, n))
