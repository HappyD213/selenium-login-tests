from selenium import webdriver


class BrowserSingleton:
    _instance = None

    def __new__(cls, options=None):
        if cls._instance is None:
            cls._instance = webdriver.Chrome(options=options)
        return cls._instance

    @classmethod
    def quit(cls):
        if cls._instance is not None:
            cls._instance.quit()
            cls._instance = None
