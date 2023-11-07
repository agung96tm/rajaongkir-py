class BasicParser:
    MAPPINGS = {}

    def __init__(self, response: dict):
        self.response = response["results"]

    def transform_key(self, key) -> str:
        if key in self.MAPPINGS:
            return self.MAPPINGS[key]["key"]
        return key

    def transform_type(self, key, value) -> str:
        if key in self.MAPPINGS:
            return self.MAPPINGS[key].get("type", lambda a: a)(value)
        return value

    def parse(self) -> list:
        results = self.response if isinstance(self.response, list) else [self.response]
        return [
            {
                self.transform_key(key): self.transform_type(key, value)
                for key, value in result.items()
            } for result in results
        ]


class ProvinceParser(BasicParser):
    MAPPINGS = {
        "province_id": {"key": "id", "type": int},
        "province": {"key": "name", "type": str},
    }


class CityParser(BasicParser):
    MAPPINGS = {
        "city_id": {"key": "id", "type": int},
        "city_name": {"key": "name", "type": str},
        "province_id": {"key": "province_id", "type": int}
    }
