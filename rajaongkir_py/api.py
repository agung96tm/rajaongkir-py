from rajaongkir_py.config import Config
from rajaongkir_py.http import get


class Rajaongkir:
    def __init__(self, key: str, account_type: str):
        self.config = Config(account_type, key)

    def get_provinces(self, **province_params) -> list:
        return get(
            base_url=self.config.get_base_url(),
            endpoint="provinces",
            headers=self.config.get_headers(),
            params=province_params,
        )

    def get_cities(self, **city_params) -> list:
        return get(
            base_url=self.config.get_base_url(),
            endpoint="provinces",
            headers=self.config.get_headers(),
            params=city_params,
        )
