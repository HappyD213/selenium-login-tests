def get_prices(locator, count):
    def _predicate(driver):
        elements = driver.find_elements(*locator)
        prices = []

        for element in elements[:count]:
            price = element.get_attribute("data-price-final")
            if price is not None:
                prices.append(int(price))
        return prices

    return _predicate
