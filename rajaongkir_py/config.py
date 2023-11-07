from rajaongkir_py.constants import ACCOUNT_TYPES, BASE_URLS


class Config:
    def __init__(self, account_type: str, key: str):
        self.account_type = account_type
        self.key = key

        self.base_url = self.get_base_url()
        self.headers = self.get_headers()

    def get_base_url(self) -> str:
        if self.account_type not in ACCOUNT_TYPES:
            raise TypeError("invalid account type")
        return BASE_URLS[self.account_type]

    def get_headers(self) -> dict:
        return {
            'key': self.key
        }
