from . import _api_client

class Stop():
    """A bus stop."""
    def __init__(self, stop_id, name, web_name, weight, lat, lon):
        self.stop_id = stop_id
        """Id of the stop."""

        self.name = name
        """Name of the stop."""

        self.web_name = web_name
        """Name of the stop as shown on the web."""

        self.weight = weight
        """Weight of the stop."""

        self.lat = lat
        """Latitude of the stop."""

        self.lon = lon
        """Longitude of the stop."""

    def __repr__(self):
        return self.name
    
def _parse_stops(data: dict) -> list[Stop]:
    stops =[]
    for el in data:
        stop = Stop(
            stop_id=el.get("parada"),
            name=el.get("nombre"),
            web_name=el.get("nom_web"),
            weight=el.get("peso"),
            lat=el.get("lat"),
            lon=el.get("lon"),
        )
        stops.append(stop)
    return stops 
   
def get_stops() -> list[Stop]:
    """
    Obtains all available bus stops.

    Returns:
        A list containing all bus stops.
    """
    return _parse_stops(_api_client.get("superparadas/index/buscador.json")["paradas"])

def get_stops_by_keywords(keywords: str) -> list[Stop]:
    """
    Obtains bus stops whose name matches the given keywords.

    Args:
        keywords: Words used to filter stops by name.

    Returns:
        A list of stops matching the given keywords.
    """
    stops = get_stops()
    keywords_list = keywords.lower().split(" ")
    return [item for item in stops if all(keyword in item.name.lower() for keyword in keywords_list)]

def get_stops_by_id(id: int) -> Stop | None:
    """
    Obtains a bus stop by its identifier.

    Args:
        id: Identifier of the bus stop.

    Returns:
        The matching bus stop if found, otherwise None.
    """
    stops = get_stops()
    for stop in stops:
        if stop.stop_id == id:
            return stop
    return None

def get_destinations_from_stop(id: int) -> list[Stop]:
    """
    Obtains all destination stops reachable from a given origin stop.

    Args:
        id: Identifier of the origin bus stop.

    Returns:
        A list of reachable destination stops.
    """
    return _parse_stops(_api_client.get(f"superparadas/por-origen/{id}/buscador.json"))