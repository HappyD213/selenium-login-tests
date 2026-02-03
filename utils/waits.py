class DocumentReady:
    def __call__(self, driver):
        try:
            return driver.execute_script("return document.readyState") == "complete"
        except:
            return False

class WaitForNElementsInContainer:
    def __init__(self, container_locator, elements_locator, count):
        self.container_locator = container_locator
        self.elements_locator = elements_locator
        self.count = count

    def __call__(self, driver):
        try:
            container = driver.find_element(*self.container_locator)
            elements = container.find_elements(*self.elements_locator)
            return len(elements) >= self.count
        except:
            return False
