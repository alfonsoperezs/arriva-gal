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
    for el in data["paradas"]:
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
    Get all lines.
    """
    return _parse_stops(_api_client.get("superparadas/index/buscador.json"))

def get_stops_by_keywords(keywords: str) -> list[Stop]:
    """
    Get lines whose name match with the given keywords
    """
    stops = get_stops()
    keywords_list = keywords.lower().split(" ")
    return [item for item in stops if all(keyword in item.name.lower() for keyword in keywords_list)]

def get_stops_by_id(id: int) -> Stop:
    stops = get_stops()
    for stop in stops:
        if stop.stop_id == id:
            return stop
    return None
    