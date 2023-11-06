from rajaongkir_py.constants import ACCOUNT_TYPES, BASE_URLS


class Config:
    def __init__(self, account_type: str, key: str):
        if not hasattr(account_type, ACCOUNT_TYPES):
            raise TypeError("invalid account type")

        self._account_type = account_type
        self._base_url = BASE_URLS[account_type]
        self._key = key

    def get_base_url(self):
        return self._base_url

    def get_headers(self):
        return {
            'key': self._key
        }

