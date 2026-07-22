from . import _api_client
from ..exceptions import ArrivaGalBusNotFoundException

class Bus:
    """A bus with its data."""

    def __init__(
        self,
        id,
        license_plate,
        brand,
        model,
        description,
        created,
        modified,
        name,
        odometer,
        date,
        platform,
        ovelan_id,
        webfleet_uid,
        active,
        emission_standard,
        emission_category,
        first_registration_date,
        seats,
        total_capacity,
        in_workshop,
        in_workshop_since,
        in_workshop_notes,
        position_ovelan,
        position_webfleet,
    ):
        self.id = id
        """Identifier of the bus."""

        self.license_plate = license_plate
        """License plate of the bus."""

        self.brand = brand
        """Manufacturer brand of the bus."""

        self.model = model
        """Model of the bus."""

        self.description = description
        """Description of the bus."""

        self.created = created
        """Date when the bus record was created."""

        self.modified = modified
        """Date when the bus record was last modified."""

        self.name = name
        """Name or identifier assigned to the bus."""

        self.odometer = odometer
        """Distance travelled by the bus."""

        self.date = date
        """Date of the latest position update."""

        self.platform = platform
        """Tracking platform used by the bus."""

        self.ovelan_id = ovelan_id
        """Ovelan identifier of the bus."""

        self.webfleet_uid = webfleet_uid
        """Webfleet unique identifier of the bus."""

        self.active = active
        """Whether the bus is currently active."""

        self.emission_standard = emission_standard
        """Emission standard classification."""

        self.emission_category = emission_category
        """Emission category classification."""

        self.first_registration_date = first_registration_date
        """Date of the first vehicle registration."""

        self.seats = seats
        """Number of seats available on the bus."""

        self.total_capacity = total_capacity
        """Total passenger capacity of the bus."""

        self.in_workshop = in_workshop
        """Whether the bus is currently in a workshop."""

        self.in_workshop_since = in_workshop_since
        """Date since the bus has been in the workshop."""

        self.in_workshop_notes = in_workshop_notes
        """Additional notes about the workshop status."""

        self.position_ovelan = position_ovelan
        """Current position data from Ovelan."""

        self.position_webfleet = position_webfleet
        """Current position data from Webfleet."""

    def __repr__(self):
        return str(self.id)
    
def _parse_bus(data: dict) -> Bus:
    return Bus(
        id=data.get("id"),
        license_plate=data.get("matricula"),
        brand=data.get("marca"),
        model=data.get("modelo"),
        description=data.get("descripcion"),
        created=data.get("created"),
        modified=data.get("modified"),
        name=data.get("name"),
        odometer=data.get("odometer"),
        date=data.get("date"),
        platform=data.get("plataforma"),
        ovelan_id=data.get("ovelan_id"),
        webfleet_uid=data.get("webfleet_uid"),
        active=data.get("activo"),
        emission_standard=data.get("normativa_emisiones"),
        emission_category=data.get("categoria_emisiones"),
        first_registration_date=data.get("fecha_primera_matriculacion"),
        seats=data.get("asientos"),
        total_capacity=data.get("plazas_totales"),
        in_workshop=data.get("en_taller"),
        in_workshop_since=data.get("en_taller_desde"),
        in_workshop_notes=data.get("en_taller_notas"),
        position_ovelan=data.get("posicion_ovelan"),
        position_webfleet=data.get("posicion_webfleet"),
    )
    
def _parse_buses(data: dict) -> list[Bus]:
    buses = []
    for el in data["buses"]:
        buses.append(_parse_bus(el))
    return buses

def get_buses() -> list[Bus]:
    """
    Obtains all available buses.

    Returns:
        A list containing all available buses.
    """
    return _parse_buses(_api_client.get("buses/getGeolocs.json"))

def get_bus_by_id(id: int) -> Bus | None:
    """
    Obtains a bus by its identifier.

    Args:
        id: Identifier of the bus.

    Returns:
        The bus matching the identifier.

    Raises:
        ArrivaGalBusNotFoundException:
            If no bus exists with the given identifier.
    """
    response = _api_client.get(f"buses/getGeoloc/{id}.json")

    if response is None:
        raise ArrivaGalBusNotFoundException(id, response)

    return _parse_bus(response)

