from selenium.webdriver.support.ui import WebDriverWait
from utils.config_reader import ConfigReader

config = ConfigReader()


class BasePage:
    def __init__(self, driver):
        self.browser = driver
        self.base_url = config.get("DEFAULT", "base_url")
        self.timeout = config.get_int("DEFAULT", "timeout")
        self.wait = WebDriverWait(driver, self.timeout, poll_frequency=0.1)
