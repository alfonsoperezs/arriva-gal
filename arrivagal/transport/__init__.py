from ..api_client import APIClient
from ..api_url import ARRIVA_URL

_api_client = APIClient(ARRIVA_URL)

from . import stops
from . import buses
from . import lines

__all__ = ["stops", "buses", "lines"]