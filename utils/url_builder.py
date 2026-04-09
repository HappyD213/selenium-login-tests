class UrlBuilder:
    @staticmethod
    def get_basic_auth_url(url: str, login: str, password: str) -> str:
        login = login
        password = password
        scheme, sep, rest = url.partition("://")
        if not sep:
            raise ValueError(f"Invalid BASE_URL: {url}")

        return f"{scheme}{sep}{login}:{password}@{rest}"
