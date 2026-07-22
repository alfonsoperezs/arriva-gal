import pytest

from arrivagal.transport.lines import (
    Line,
    _parse_line,
    _parse_lines,
    get_lines,
    get_line_by_id,
)
from arrivagal.exceptions import ArrivaGalLineNotFoundException


LINE_DATA = {
    "id": 493,
    "conc_admin_l": 848,
    "lineas": 10368,
    "nom_linea": "Coruña E.A.-Fisterra",
    "par_ori": 257,
    "par_des": 875,
    "Descripcion_Web_Ida": "CORUÑA E.A.-FISTERRA",
    "Descripcion_Web_Vuelta": "FISTERRA-CORUÑA E.A.",
    "fecha_desde": "2020-12-23T00:00:00+01:00",
    "fecha_hasta": "3000-12-12T23:59:59+01:00",
}


def test_parse_line():
    line = _parse_line(LINE_DATA)

    assert isinstance(line, Line)
    assert line.id == 493
    assert line.administrative_id == 848
    assert line.code == 10368
    assert line.name == "Coruña E.A.-Fisterra"
    assert line.origin_stop_id == 257
    assert line.destination_stop_id == 875
    assert line.outbound_description == "CORUÑA E.A.-FISTERRA"
    assert line.return_description == "FISTERRA-CORUÑA E.A."
    assert line.valid_from == "2020-12-23T00:00:00+01:00"
    assert line.valid_until == "3000-12-12T23:59:59+01:00"


def test_parse_lines():
    data = {
        "lineas": [
            LINE_DATA,
            {
                **LINE_DATA,
                "id": 500,
                "nom_linea": "Otra línea",
            },
        ]
    }

    lines = _parse_lines(data)

    assert len(lines) == 2
    assert lines[0].id == 493
    assert lines[1].name == "Otra línea"


def test_get_lines(monkeypatch):
    monkeypatch.setattr(
        "arrivagal.transport.lines._api_client.get",
        lambda url: {"lineas": [LINE_DATA]}
    )

    lines = get_lines()

    assert len(lines) == 1
    assert isinstance(lines[0], Line)
    assert lines[0].id == 493


def test_get_line_by_id(monkeypatch):
    monkeypatch.setattr(
        "arrivagal.transport.lines._api_client.get",
        lambda url: {"linea": LINE_DATA}
    )

    line = get_line_by_id(493)

    assert isinstance(line, Line)
    assert line.id == 493
    assert line.name == "Coruña E.A.-Fisterra"


def test_get_line_by_id_not_found(monkeypatch):
    monkeypatch.setattr(
        "arrivagal.transport.lines._api_client.get",
        lambda url: {"linea": None}
    )

    with pytest.raises(ArrivaGalLineNotFoundException):
        get_line_by_id(999)