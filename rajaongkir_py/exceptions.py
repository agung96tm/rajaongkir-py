from typing import Optional, Union

from requests import HTTPError


class RajaongkirPyError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class RajaongkirException(Exception):
    def __init__(self, response: Optional[Union[HTTPError, RajaongkirPyError]]):
        self.status_code = None
        self.message = None
        self.error_type = None

        self.response = response
        self.error_handler()

    def error_handler(self) -> None:
        if isinstance(self.response, HTTPError):
            self.status_code = self.response.response.status_code
            self.message = str(self.response)
            self.error_type = "RajaongkirError"
        else:
            self.status_code = self.response.status_code
            self.message = str(self.response.message)
            self.error_type = "RajaongkirPyError"

    def __repr__(self):
        return f"<{self.error_type} ({self.status_code}): {self.message}>"

    def __str__(self):
        return self.__repr__()
