import pytest
from selenium import webdriver

from utils.browser_singleton import BrowserSingleton


@pytest.fixture
def browser(request):
    language = request.param
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={language}")
    driver = BrowserSingleton(options=options)
    yield driver
    BrowserSingleton.quit()
