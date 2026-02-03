import pytest
from selenium import webdriver

class SingletonBrowser:
    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonBrowser, cls).__new__(cls)
        return cls._instance

    @property
    def driver(self):
        if self._driver is None:
            self._driver = webdriver.Chrome()
        return self._driver

    def quit(self):
        if self._driver:
            self._driver.quit()
            self._driver = None

@pytest.fixture(scope="session")
def browser():
    browser_instance = SingletonBrowser()
    yield browser_instance.driver
    browser_instance.quit()
