import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory


@pytest.fixture
def browser():
    options = [
        "--headless=new",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--window-size=1920,1080",
    ]
    driver = BrowserFactory().get_driver(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
