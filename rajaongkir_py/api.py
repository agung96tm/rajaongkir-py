from typing import Union

from rajaongkir_py.config import Config
from rajaongkir_py.exceptions import RajaongkirException, RajaongkirPyError
from rajaongkir_py.http import get
from rajaongkir_py.params import CityParams, ProvinceParams
from rajaongkir_py.parsers import ProvinceParser, CityParser


class Rajaongkir:
    def __init__(self, key: str, account_type: str):
        self.config = Config(account_type=account_type, key=key)

    def get_provinces(self, **params) -> list:
        params = ProvinceParams(params).get_params()
        response = get(self.config.base_url, "province", self.config.headers, params)
        return ProvinceParser(response).parse()

    def get_cities(self, **params) -> list:
        params = CityParams(params).get_params()
        response = get(self.config.base_url, "city", self.config.headers, params)
        return CityParser(response).parse()

    def get_province(self, id, raise_error=False, params=None) -> Union[dict, None]:
        params = ProvinceParams(params or {}).get_params()
        cities = self.get_provinces(id=id, **params)

        if raise_error and len(cities) == 0:
            raise RajaongkirException(response=RajaongkirPyError(
                status_code=404,
                message="city not found",
            ))
        return cities[0] if len(cities) > 0 else None

    def get_city(self, id, raise_error=False, params=None) -> Union[dict, None]:
        params = CityParams(params or {}).get_params()
        cities = self.get_cities(id=id, **params)

        if raise_error and len(cities) == 0:
            raise RajaongkirException(response=RajaongkirPyError(
                status_code=404,
                message="city not found",
            ))
        return cities[0] if len(cities) > 0 else None
