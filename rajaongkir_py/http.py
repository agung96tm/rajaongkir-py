import json
from typing import Optional, Union
import requests

from rajaongkir_py.exceptions import RajaongkirException


def parse_response(data: dict) -> list:
    if "rajaongkir" in data:
        results = data["rajaongkir"]["results"]
        return results if isinstance(results, list) else [results]
    return []


def get(base_url: str, endpoint: str, headers: Optional[Union[str, int]], params: any) -> list:
    url = "/".join([base_url, endpoint])

    try:
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
        resp_json = resp.json()
        return parse_response(data=resp_json)
    except requests.exceptions.HTTPError as e:
        raise RajaongkirException(
            code=400,
            message=str(e),
        )
    except json.JSONDecodeError:
        raise RajaongkirException(
            code="json decoder",
            message="fail to decode response",
        )
