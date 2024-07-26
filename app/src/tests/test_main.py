import pytest
from ..service.services import Services
from ..utils.ETL import Utils


# client = TestClient(app)

services = Services()

utils = Utils()


# @pytest.mark.anyio
# @mock.patch("client.get")
# async def test_read_value(mock_exchange_json):
#     mock_exchange_json.return_value = 200
#     response = client.get("/api/convert/BRL/579")
#     assert response.status_code == 200
#     assert response.json() == {"USD": 117.31, "EUR": 110.13, "INR": 9727.2}


# @pytest.mark.anyio
# async def test__item_inexist():
#     response = client.get("/api/convert/USD/579")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Not Found"}


@pytest.mark.anyio
def test_transform_input():
    # entrada = "BRL-USD,BRL-EUR,BRL-INR"
    input_one = {"BRLUSD": 117.25, "BRLEUR": 110.13, "BRLINR": 9727.2}
    # esperado = ["BRLUSD", "BRLEUR", "BRLINR"]
    expect = {"USD": 117.25, "EUR": 110.13, "INR": 9727.2}
    result = utils.transform_input(input_one)

    assert result == expect


@pytest.mark.anyio
def test_extract_json():
    input_one = {
        "BRLUSD": {
            "code": "BRL",
            "codein": "USD",
            "name": "Real Brasileiro/Dólar Americano",
            "high": "0.2026",
            "low": "0.2026",
            "varBid": "0",
            "pctChange": "0",
            "bid": "0.2025",
            "ask": "0.2026",
            "timestamp": "1695360572",
            "create_date": "2023-09-22 02:29:32",
        },
        "BRLEUR": {
            "code": "BRL",
            "codein": "EUR",
            "name": "Real Brasileiro/Euro",
            "high": "0.1903",
            "low": "0.19",
            "varBid": "0.0002",
            "pctChange": "0.13",
            "bid": "0.1901",
            "ask": "0.1902",
            "timestamp": "1695360603",
            "create_date": "2023-09-22 02:30:03",
        },
        "BRLINR": {
            "code": "BRL",
            "codein": "INR",
            "name": "Real Brasileiro/Rúpia Indiana",
            "high": "16.84",
            "low": "16.77",
            "varBid": "-0.03",
            "pctChange": "-0.19",
            "bid": "16.79",
            "ask": "16.8",
            "timestamp": "1695360589",
            "create_date": "2023-09-22 02:29:49",
        },
    }
    input_two = ["BRLUSD", "BRLEUR", "BRLINR"]
    input_three = "bid"
    expect = {"BRLUSD": "0.2025", "BRLEUR": "0.1901", "BRLINR": "16.79"}
    result = services.extract_json(input_one, input_two, input_three)
    assert expect == result


@pytest.mark.anyio
def test_converter_valores():
    input_one = 579
    input_two = {"BRLUSD": "0.2026", "BRLEUR": "0.1902", "BRLINR": "16.8"}
    expect = {"BRLUSD": 117.31, "BRLEUR": 110.13, "BRLINR": 9727.2}
    result = services.convert_values(input_one, input_two)
    assert expect == result
