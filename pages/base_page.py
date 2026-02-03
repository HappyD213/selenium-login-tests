from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import DocumentReady, WaitForNElementsInContainer

class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)

    def open(self, url):
        self.browser.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_ready_state(self):
        self.wait.until(DocumentReady())

    def wait_for_n_elements(self, container_locator, elements_locator, count):
        self.wait.until(WaitForNElementsInContainer(container_locator, elements_locator, count))

