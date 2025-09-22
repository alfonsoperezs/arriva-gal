from ..api_client import APIClient
from ..api_url import ARRIVA_URL

_api_client = APIClient(ARRIVA_URL)

from . import stops

__all__ = ["stops"]