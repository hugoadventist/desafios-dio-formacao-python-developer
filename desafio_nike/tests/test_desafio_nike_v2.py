from src.desafio_nike_v2 import (
    transformar_entrada,
    extrair_dados_json,
    converter_valores,
    app,
)

from fastapi.testclient import TestClient


def test_transformar_entrada():
    # entrada = "BRL-USD,BRL-EUR,BRL-INR"
    entrada = {"BRLUSD": 117.25, "BRLEUR": 110.13, "BRLINR": 9727.2}
    # esperado = ["BRLUSD", "BRLEUR", "BRLINR"]
    esperado = {"USD": 117.25, "EUR": 110.13, "INR": 9727.2}
    resultado = transformar_entrada(entrada)

    assert resultado == esperado


def test_extrair_dados_json():
    entrada_um = {
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
    entrada_dois = ["BRLUSD", "BRLEUR", "BRLINR"]
    entrada_tres = "bid"
    esperado = {"BRLUSD": "0.2025", "BRLEUR": "0.1901", "BRLINR": "16.79"}
    resultado = extrair_dados_json(entrada_um, entrada_dois, entrada_tres)
    assert esperado == resultado


def test_converter_valores():
    entrada_um = 579
    entrada_dois = {"BRLUSD": "0.2026", "BRLEUR": "0.1902", "BRLINR": "16.8"}
    esperado = {"BRLUSD": 117.31, "BRLEUR": 110.13, "BRLINR": 9727.2}
    resultado = converter_valores(entrada_um, entrada_dois)
    assert esperado == resultado


client = TestClient(app)


def teste_receber_valor():
    response = client.get("/api/convert/BRL/579")
    assert response.status_code == 200
    assert response.json() == {"USD": 117.31, "EUR": 110.13, "INR": 9727.2}


def teste_item_inexistente():
    response = client.get("/api/convert/USD/579")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
