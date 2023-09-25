"""API to convert currencies at BRL to another one.

Returns:
    dict: a json file currencies converted from BRL.
"""
from fastapi import FastAPI
import aiohttp
import uvicorn

app = FastAPI()


def transformar_entrada(entradas: str | dict) -> list | dict:
    """Receive a string, extract all hyphens and returns a list with each element that
    is separated by commas.

    Returns:
       list: list of currencies to convert.
       dict: list of currencies converted.
    """
    if isinstance(entradas, str):
        output = entradas.replace("-", "").split(",")
    if isinstance(entradas, dict):
        new_keys = [key.replace("BRL", "") for key in entradas]
        output = dict(zip(new_keys, entradas.values()))
    return output


def extrair_dados_json(json_file: dict, coins: list, key: str) -> dict:
    """Extract data of a json file and return a new json

    Returns:
        dict: data with currency exchanges.
    """

    return {currency: json_file[currency][key] for currency in coins}


def converter_valores(value: float, last_exchange: dict) -> dict:
    """Convert currency values of a json file and return the json with
    desired conversion.

    Returns:
        dict: the values of currencies converted.
    """
    for currency in last_exchange:
        last_exchange[currency] = float(last_exchange[currency])
        last_exchange[currency] *= value
    return {key: round(last_exchange[key], 2) for key in last_exchange}


@app.get("/api/convert/BRL/{valor}", status_code=200)
async def receber_valor(valor: float, moedas: str = "BRL-USD,BRL-EUR,BRL-INR") -> dict:
    """Receive the path parameter and default to query parameter containing
    "BRL-USD,BRL-EUR,BRL-INR".

    Args:
        valor (float): Value in R$ to convert.
        moedas (str, optional): the query parameter with desired currencies.
        Defaults to "BRL-USD,BRL-EUR,BRL-INR".

    Returns:
        dict: the json file with currency conversion done.
    """
    if moedas:
        moedas += ",BRL-USD,BRL-EUR,BRL-INR"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://economia.awesomeapi.com.br/last/" + moedas, raise_for_status=True
        ) as resp:
            print(resp.status)
            exchange_json = await resp.json()

    # exchange_json = json.dumps(resp, sort_keys=False, indent=4)
    currency_list = transformar_entrada(moedas)
    print(currency_list)

    valores_moedas = extrair_dados_json(
        json_file=exchange_json, coins=currency_list, key="bid"
    ).copy()

    print("Valor total: ", valores_moedas)

    valores_convertidos = transformar_entrada(converter_valores(valor, valores_moedas))

    return valores_convertidos


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
