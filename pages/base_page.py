from utils.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait

config = ConfigReader()


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = config.get_int("DEFAULT", "timeout")
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.fast_wait = WebDriverWait(self.driver, self.timeout, poll_frequency=0.1)
