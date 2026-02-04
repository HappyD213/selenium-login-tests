import pytest
from utils.browser import  Browser

@pytest.fixture(scope="session")
def browser():
    driver = Browser()
    yield driver
    driver.quit()