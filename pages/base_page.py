from selenium.webdriver.support.ui import WebDriverWait

from utils.browser_singleton import BrowserSingleton
from utils.config_reader import ConfigReader

config = ConfigReader()


class BasePage:
    def __init__(self):
        self.driver = BrowserSingleton()
        self.timeout = config.get_int("DEFAULT", "timeout")
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.fast_wait = WebDriverWait(self.driver, self.timeout, poll_frequency=0.1)
