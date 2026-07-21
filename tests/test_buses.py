import pytest
from unittest.mock import Mock, patch

from arrivagal.transport.buses import (
    Bus,
    get_buses,
    get_bus_by_id,
)
from arrivagal.exceptions import ArrivaGalBusNotFoundException


def test_get_bus_by_id_returns_bus():
    mock_response = {
        "id": 123,
        "matricula": "1234ABC",
        "marca": "MAN",
        "modelo": "Lion's City",
        "activo": True,
    }

    with patch("arrivagal.transport.buses._api_client.get", return_value=mock_response):
        bus = get_bus_by_id(123)

    assert isinstance(bus, Bus)
    assert bus.id == 123
    assert bus.license_plate == "1234ABC"
    assert bus.brand == "MAN"


def test_get_bus_by_id_not_found():
    with patch("arrivagal.transport.buses._api_client.get", return_value=None):
        with pytest.raises(ArrivaGalBusNotFoundException):
            get_bus_by_id(999)


def test_get_buses():
    mock_response = {
        "buses": [
            {
                "id": 1,
                "matricula": "1111AAA",
                "marca": "MAN",
            },
            {
                "id": 2,
                "matricula": "2222BBB",
                "marca": "Mercedes",
            },
        ]
    }

    with patch("arrivagal.transport.buses._api_client.get", return_value=mock_response):
        buses = get_buses()

    assert len(buses) == 2
    assert buses[0].id == 1
    assert buses[1].brand == "Mercedes"