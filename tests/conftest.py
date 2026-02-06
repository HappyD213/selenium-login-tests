import pytest
from utils.browser import BrowserSingleton


@pytest.fixture(scope="session")
def browser():
    driver = BrowserSingleton()
    yield driver
    driver.quit()
