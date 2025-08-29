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
            stop_id=el.get("id"),
            name=el.get("name"),
            web_name=el.get("webName"),
            weight=el.get("weight"),
            lat=el.get("lat"),
            lon=el.get("lon"),
        )
        stops.append(stop)
    return stops 
   
def get_stops():
    return _parse_stops(_api_client.get("superparadas/index/buscador.json"))
    