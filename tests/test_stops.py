from unittest.mock import patch

from arrivagal.transport.stops import (
    Stop,
    get_stops,
    get_stops_by_keywords,
    get_stops_by_id,
    get_destinations_from_stop,
)


def test_get_stops():
    mock_response = {
        "paradas": [
            {
                "parada": 1,
                "nombre": "Plaza Galicia",
                "nom_web": "Plaza Galicia",
                "peso": 10,
                "lat": 43.36,
                "lon": -8.41,
            },
            {
                "parada": 2,
                "nombre": "Universidad",
                "nom_web": "Universidade",
                "peso": 5,
                "lat": 43.33,
                "lon": -8.41,
            }
        ]
    }

    with patch(
        "arrivagal.transport.stops._api_client.get",
        return_value=mock_response
    ):
        stops = get_stops()

    assert len(stops) == 2
    assert isinstance(stops[0], Stop)
    assert stops[0].stop_id == 1
    assert stops[0].name == "Plaza Galicia"


def test_get_stops_by_keywords():
    mock_response = {
        "paradas": [
            {
                "parada": 1,
                "nombre": "Plaza Galicia",
                "nom_web": "Plaza Galicia",
                "peso": 10,
                "lat": 0,
                "lon": 0,
            },
            {
                "parada": 2,
                "nombre": "Universidad",
                "nom_web": "Universidad",
                "peso": 5,
                "lat": 0,
                "lon": 0,
            }
        ]
    }

    with patch(
        "arrivagal.transport.stops._api_client.get",
        return_value=mock_response
    ):
        stops = get_stops_by_keywords("plaza galicia")

    assert len(stops) == 1
    assert stops[0].name == "Plaza Galicia"


def test_get_stops_by_id_found():
    mock_response = {
        "paradas": [
            {
                "parada": 123,
                "nombre": "Riazor",
                "nom_web": "Riazor",
                "peso": 1,
                "lat": 0,
                "lon": 0,
            }
        ]
    }

    with patch(
        "arrivagal.transport.stops._api_client.get",
        return_value=mock_response
    ):
        stop = get_stops_by_id(123)

    assert stop.stop_id == 123
    assert stop.name == "Riazor"


def test_get_stops_by_id_not_found():
    with patch(
        "arrivagal.transport.stops._api_client.get",
        return_value={"paradas": []}
    ):
        stop = get_stops_by_id(999)

    assert stop is None


def test_get_destinations_from_stop():
    mock_response = [
        {
            "parada": 10,
            "nombre": "Destino",
            "nom_web": "Destino",
            "peso": 1,
            "lat": 0,
            "lon": 0,
        }
    ]

    with patch(
        "arrivagal.transport.stops._api_client.get",
        return_value=mock_response
    ):
        destinations = get_destinations_from_stop(1)

    assert len(destinations) == 1
    assert destinations[0].stop_id == 10