from fastapi import FastAPI, Response, status
import aiohttp
from aiohttp import web
import uvicorn

app = FastAPI()


def transformar_entrada(entradas: str):
    saidas = entradas.replace("-", "").split(",")
    return saidas


def extrair_dados_json(json_file: dict, coins: list, key: str):
    exchange_rates = {}
    for currency in coins:
        exchange_rates[currency] = json_file[currency][key]
    return exchange_rates


def converter_valores(value: float, last_exchange: dict):
    for currency in last_exchange:
        last_exchange[currency] = float(last_exchange[currency])
        last_exchange[currency] *= value
    return {key: round(last_exchange[key], 2) for key in last_exchange}


@app.get("/api/convert/BRL/{valor}", status_code=200)
async def receber_valor(valor: float, moedas: str = "BRL-USD,BRL-EUR,BRL-INR"):
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

    valores_convertidos = converter_valores(valor, valores_moedas)

    return valores_convertidos


if __name__ == "__main__":
    uvicorn.run(app, port=8000)

# exchanges = aiohttp.request(
#     "GET", "https://economia.awesomeapi.com.br/last/BRL-USD,BRL-EUR,BRL-INR"
# )
