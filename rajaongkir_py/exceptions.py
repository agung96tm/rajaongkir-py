class RajaongkirException(Exception):
    def __init__(self, code, message):
        self._code = code
        self._message = message

    def __str__(self):
        return f"<Rajaongkir Exception ({self._code}): {self._message}>"
