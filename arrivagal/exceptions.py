class ArrivaGalBaseException(Exception):
    def __init__(self, message, response=None):
        self.message = message
        self.response = response
        super().__init__(message)


class ArrivaGalBusNotFoundException(ArrivaGalBaseException):
    """
    Exception used when the server returns null on bus endpoint (it doesn't exist).
    """
    def __init__(self, bus_id, response=None):
        super().__init__(f"Bus with ID '{bus_id}' was not found.", response)


class ArrivaGalLineNotFoundException(ArrivaGalBaseException):
    """
    Exception used when the server returns null on line endpoint (it doesn't exist).
    """
    def __init__(self, id, response=None):
        super().__init__(f"Line with ID '{id}' was not found.", response)

class ArrivaGalExpeditionNotFoundException(ArrivaGalBaseException):
    """
    Exception used when the server returns null on expedition endpoint (it doesn't exist).
    """
    def __init__(self, id, response=None):
        super().__init__(f"Expedition with ID '{id}' was not found.", response)