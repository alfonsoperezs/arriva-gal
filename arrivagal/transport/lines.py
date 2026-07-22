from . import _api_client
from ..exceptions import ArrivaGalLineNotFoundException

class Line():
    """A bus line."""
    def __init__(
        self,
        id,
        administrative_id,
        code,
        name,
        origin_stop_id,
        destination_stop_id,
        outbound_description,
        return_description,
        valid_from,
        valid_until,
    ):
        self.id = id
        """Id of the line."""

        self.administrative_id = administrative_id
        """Administrative identifier of the line."""

        self.code = code
        """Internal code of the line."""

        self.name = name
        """Name of the line."""

        self.origin_stop_id = origin_stop_id
        """Id of the origin stop."""

        self.destination_stop_id = destination_stop_id
        """Id of the destination stop."""

        self.outbound_description = outbound_description
        """Description of the outbound direction."""

        self.return_description = return_description
        """Description of the return direction."""

        self.valid_from = valid_from
        """Date from which the line is valid."""

        self.valid_until = valid_until
        """Date until which the line is valid."""

    def __repr__(self):
        return self.name


def _parse_line(data: dict) -> Line:
    return Line(
        id=data.get("id"),
        administrative_id=data.get("conc_admin_l"),
        code=data.get("lineas"),
        name=data.get("nom_linea"),
        origin_stop_id=data.get("par_ori"),
        destination_stop_id=data.get("par_des"),
        outbound_description=data.get("Descripcion_Web_Ida"),
        return_description=data.get("Descripcion_Web_Vuelta"),
        valid_from=data.get("fecha_desde"),
        valid_until=data.get("fecha_hasta"),
    )


def _parse_lines(data: dict) -> list[Line]:
    lines = []
    for el in data["lineas"]:
        lines.append(_parse_line(el))
    return lines

def get_lines() -> list[Line]:
    """
    Get all available bus lines.

    Returns:
        A list containing all bus lines.
    """
    return _parse_lines(_api_client.get("lineas/index.json"))

def get_line_by_id(id: int) -> Line:
    """
    Get a bus line by its id.

    Args:
        id: The identifier of the line to retrieve.

    Returns:
        The requested bus line.

    Raises:
        ArrivaGalLineNotFoundException: If no line exists with the given id.
    """
    response = _api_client.get(f"lineas/view/{id}.json")

    if response["linea"] is None:
        raise ArrivaGalLineNotFoundException(id, response)
    
    return _parse_line(response["linea"])

def get_lines_by_keywords(keywords: str) -> list[Line]:
    """
    Get bus lines whose name matches the given keywords.

    The search is case-insensitive and all provided keywords must be
    contained in the line name.

    Args:
        keywords: Keywords to search for in the line name.

    Returns:
        A list of bus lines matching the given keywords.
    """
    lines = get_lines()
    keywords_list = keywords.lower().split(" ")
    return [item for item in lines if all(keyword in item.name.lower() for keyword in keywords_list)]
