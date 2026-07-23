from . import _api_client
from datetime import datetime
from ..exceptions import ArrivaGalExpeditionNotFoundException

class Expedition:
    """A bus expedition."""

    def __init__(
        self,
        id,
        code,
        line_code,
        name,
        short_name,
        origin_stop_id,
        destination_stop_id,
        origin_ordinal,
        destination_ordinal,
        direction,
        weekly_frequency,
        annual_season,
        departure_time,
        arrival_time,
        valid_from,
        valid_until,
        description,
        line_id,
    ):
        self.id = id
        """Id of the expedition."""

        self.code = code
        """Internal expedition code."""

        self.line_code = line_code
        """Internal code of the associated line."""

        self.name = name
        """Name of the expedition."""

        self.short_name = short_name
        """Short name of the expedition."""

        self.origin_stop_id = origin_stop_id
        """Id of the origin stop."""

        self.destination_stop_id = destination_stop_id
        """Id of the destination stop."""

        self.origin_ordinal = origin_ordinal
        """Position of the origin stop within the route."""

        self.destination_ordinal = destination_ordinal
        """Position of the destination stop within the route."""

        self.direction = direction
        """Direction of travel."""

        self.weekly_frequency = weekly_frequency
        """Weekly frequency identifier."""

        self.annual_season = annual_season
        """Annual season identifier."""

        self.departure_time = departure_time
        """Scheduled departure time."""

        self.arrival_time = arrival_time
        """Scheduled arrival time."""

        self.valid_from = valid_from
        """Date from which the expedition is valid."""

        self.valid_until = valid_until
        """Date until which the expedition is valid."""

        self.description = description
        """Description shown on the web."""

        self.line_id = line_id
        """Id of the associated line."""

    def __repr__(self):
        return self.name

def _parse_expedition(data: dict) -> Expedition:
    return Expedition(
        id=data.get("id"),
        code=data.get("expediciones"),
        line_code=data.get("linea_exped"),
        name=data.get("nom_exped"),
        short_name=data.get("nom_exped_abrev"),
        origin_stop_id=data.get("id_par_origen"),
        destination_stop_id=data.get("id_par_destino"),
        origin_ordinal=data.get("ord_origen"),
        destination_ordinal=data.get("ord_destino"),
        direction=data.get("sentido"),
        weekly_frequency=data.get("frec_sem_exped"),
        annual_season=data.get("temp_anu_exped"),
        departure_time=data.get("hora_salida"),
        arrival_time=data.get("hora_llegada"),
        valid_from=data.get("fecha_desde"),
        valid_until=data.get("fecha_hasta"),
        description=data.get("Descripcion_Web"),
        line_id=data.get("linea_id"),
    )

def _parse_expeditions(data: list[dict]) -> list[Expedition]:
    expeditions = []
    for expedition in data:
        expeditions.append(_parse_expedition(expedition))
    return expeditions

def _validate_date(date: str):
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Date must have format DD-MM-YYYY")

def get_expeditions(origin_stop_id: int, destination_stop_id: int, date: str) -> list[Expedition]:
    """
    Get available expeditions between two bus stops on a specific date.

    The search includes both outbound and return directions.

    Args:
        origin_stop_id: Identifier of the origin stop.
        destination_stop_id: Identifier of the destination stop.
        date: Date of the journey in DD-MM-YYYY format.

    Returns:
        A list containing the available expeditions.

    Raises:
        ValueError: If the date format is invalid.
    """
    _validate_date(date)
    response = _api_client.get(f"buscador/search/{origin_stop_id}/{destination_stop_id}/{date}.json")
    expeditions = response["expediciones"]["ida"] + response["expediciones"]["vuelta"]
    return _parse_expeditions(expeditions)

def get_expedition_by_id(id: int) -> Expedition | None:
    """
    Get an expedition by its identifier.

    Args:
        id: Identifier of the expedition.

    Returns:
        The requested expedition if it exists, otherwise None.
    """
    response = _api_client.get(f"expediciones/get/{id}.json")

    if response["expedicion"] is None:
        raise ArrivaGalExpeditionNotFoundException(id, response)
    
    return _parse_expedition(response["expedicion"])