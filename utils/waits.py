import re
import time
from decimal import Decimal


class DocumentReady:
    def __call__(self, driver):
        try:
            return driver.execute_script("return document.readyState") == "complete"
        except:
            return False


class GetPrices:
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        try:
            elements = driver.find_elements(*self.locator)
            if len(elements) < self.count:
                return False

            elements = elements[:self.count]
            prices = []

            for element in elements:
                element_price = element.get_attribute("data-price-final")
                if element_price is None:
                    raise AssertionError(
                        "data-price-final attribute not found"
                    )
                if element_price != "0":
                    prices.append(int(element_price))

            return prices
        except:
            return False


class LoaderIsVisible:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            loader = driver.find_element(*self.locator)
            opacity = loader.value_of_css_property("opacity")
            return loader if opacity == "0.5" else False

        except:
            return False
