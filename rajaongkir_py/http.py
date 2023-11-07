import requests

from rajaongkir_py.exceptions import RajaongkirException


def get(base_url: str, path: str, headers: dict, params: any) -> dict:
    url = "/".join([base_url, path])

    try:
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
        return resp.json()["rajaongkir"]
    except requests.exceptions.HTTPError as e:
        raise RajaongkirException(e)
