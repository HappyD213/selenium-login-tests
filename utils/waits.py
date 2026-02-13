class DocumentReady:
    def __call__(self, driver):
        try:
            return driver.execute_script("return document.readyState") == "complete"
        except:
            return False
