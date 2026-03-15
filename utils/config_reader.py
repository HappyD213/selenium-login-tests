import configparser


class ConfigReader:
    BASE_CONFIG = "configs/config.ini"

    def __init__(self, config_path=BASE_CONFIG):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)
