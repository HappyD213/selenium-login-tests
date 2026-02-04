from selenium import webdriver

class Browser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = webdriver.Chrome()
        return cls._instance

