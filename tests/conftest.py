import pytest
from browser.browser import Browser
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
