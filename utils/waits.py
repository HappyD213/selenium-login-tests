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
                    raise ValueError(
                        "data-price-final attribute not found"
                    )
                if element_price != "0":
                    prices.append(int(element_price))

            return prices
        except:
            return False
