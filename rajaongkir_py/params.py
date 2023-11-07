class BasicParams:
    MAPPINGS = {}

    def __init__(self, response: dict):
        self.response = response

    def transform_key(self, key):
        if key in self.MAPPINGS:
            return self.MAPPINGS[key].get("key", key)
        return key

    def transform_type(self, key, value):
        if key in self.MAPPINGS:
            return self.MAPPINGS[key].get("type", lambda a: a)(value)
        return value

    def get_params(self) -> dict:
        return {
            self.transform_key(key): self.transform_type(key, value)
            for key, value in self.response.items()
        }


class ProvinceParams(BasicParams):
    MAPPINGS = {
        'id': {'key': 'id'}
    }


class CityParams(BasicParams):
    MAPPINGS = {
        'id': {'key': 'id'},
        'province_id': {'key': 'province'},
    }
