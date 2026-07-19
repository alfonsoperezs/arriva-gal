from . import _api_client

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
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.description = description
        self.created = created
        self.modified = modified
        self.name = name
        self.odometer = odometer
        self.date = date
        self.platform = platform
        self.ovelan_id = ovelan_id
        self.webfleet_uid = webfleet_uid
        self.active = active
        self.emission_standard = emission_standard
        self.emission_category = emission_category
        self.first_registration_date = first_registration_date
        self.seats = seats
        self.total_capacity = total_capacity
        self.in_workshop = in_workshop
        self.in_workshop_since = in_workshop_since
        self.in_workshop_notes = in_workshop_notes
        self.position_ovelan = position_ovelan
        self.position_webfleet = position_webfleet

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
    Obtains all buses.
    """
    return _parse_buses(_api_client.get("buses/getGeolocs.json"))

def get_bus_by_id(id: int) -> Bus | None:
    """
    Obtains a bus by its id.
    """
    return _parse_bus(_api_client.get(f"buses/getGeoloc/{id}.json"))

