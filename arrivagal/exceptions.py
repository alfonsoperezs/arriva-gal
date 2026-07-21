class ArrivaGalBaseException(Exception):
    """Base exception for all ArrivaGal errors."""
    def __init__(self, message, response=None):
        self.message = message
        if response is not None:
            message = (
                f"HTTP {response.status_code} {response.reason}: {message}"
            )
        super().__init__(message)

class ArrivaGalBusNotFoundException(ArrivaGalBaseException):
    """
    Exception used when the server returns null on bus endpoint (it doesn't exist)
    """
    def __init__(self, bus_id, response):
        super().__init__(f"Bus with ID '{bus_id}' was not found.", response)
