import pytest
from unittest.mock import patch

from arrivagal.transport.expeditions import (
    Expedition,
    _parse_expedition,
    _parse_expeditions,
    get_expeditions,
    get_expedition_by_id,
)
from arrivagal.exceptions import ArrivaGalExpeditionNotFoundException


EXPEDITION_DATA = {
    "id": 6317,
    "expediciones": 112957,
    "linea_exped": 10399,
    "nom_exped": "Coruña E.A.-Arteixo",
    "origen": 154833,
    "destino": 155272,
    "hora_salida": "2025-01-07T06:30:00+01:00",
    "hora_llegada": "2025-01-07T07:08:00+01:00",
    "Descripcion_Web": "Coruña E.A. - Arteixo",
}


def test_parse_expedition():
    expedition = _parse_expedition(EXPEDITION_DATA)

    assert isinstance(expedition, Expedition)
    assert expedition.id == 6317
    assert expedition.name == "Coruña E.A.-Arteixo"


def test_parse_expeditions():
    expeditions = _parse_expeditions([EXPEDITION_DATA])

    assert len(expeditions) == 1
    assert isinstance(expeditions[0], Expedition)


def test_get_expeditions():
    response = {
        "expediciones": {
            "ida": [EXPEDITION_DATA],
            "vuelta": [EXPEDITION_DATA]
        }
    }

    with patch(
        "arrivagal.transport.expeditions._api_client.get",
        return_value=response
    ):
        expeditions = get_expeditions(
            5274,
            4802,
            "07-01-2025"
        )

    assert len(expeditions) == 2
    assert expeditions[0].id == 6317


def test_get_expeditions_invalid_date():
    with pytest.raises(ValueError):
        get_expeditions(
            5274,
            4802,
            "2025-01-07"
        )


def test_get_expedition_by_id():
    response = {
        "expedicion": EXPEDITION_DATA
    }

    with patch(
        "arrivagal.transport.expeditions._api_client.get",
        return_value=response
    ):
        expedition = get_expedition_by_id(6317)

    assert isinstance(expedition, Expedition)
    assert expedition.id == 6317


def test_get_expedition_by_id_not_found():
    response = {
        "expedicion": None
    }

    with patch(
        "arrivagal.transport.expeditions._api_client.get",
        return_value=response
    ):
        with pytest.raises(ArrivaGalExpeditionNotFoundException):
            get_expedition_by_id(999)