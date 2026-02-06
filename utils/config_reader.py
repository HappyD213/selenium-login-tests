import configparser


class ConfigReader:
    def __init__(self, file_path="configs/config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)
