import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
