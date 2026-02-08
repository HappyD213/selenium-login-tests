import pytest
from utils.browser_singleton import BrowserSingleton


@pytest.fixture
def browser():
    driver = BrowserSingleton()
    yield driver
    driver.quit()
    BrowserSingleton._instance = None

