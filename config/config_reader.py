from config.config import Options


class ConfigReader:
    @staticmethod
    def get_base_url() -> str:
        return Options.BASE_URL

    @staticmethod
    def get_alerts_url() -> str:
        return Options.ALERTS_URL

    @staticmethod
    def get_context_alerts_url() -> str:
        return Options.CONTEXT_ALERTS_URL

    @staticmethod
    def get_slider_url() -> str:
        return Options.SLIDER_URL

    @staticmethod
    def get_hovers_url() -> str:
        return Options.HOVERS_URL

    @staticmethod
    def get_handlers_url() -> str:
        return Options.HANDLERS_URL

    @staticmethod
    def get_iframe_url() -> str:
        return Options.IFRAME_URL

    @staticmethod
    def get_login() -> str:
        return Options.LOGIN

    @staticmethod
    def get_password() -> str:
        return Options.PASSWORD
