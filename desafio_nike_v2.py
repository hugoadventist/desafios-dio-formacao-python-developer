from fastapi import FastAPI
import aiohttp
import currencies

app = FastAPI()

currencies_path = currencies.parser_currencies()


@app.get("/api/convert/BRL/{valor}")
async def converter_value(valor: float):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://economia.awesomeapi.com.br/last/" + currencies_path
        ) as resp:
            print(resp.status)
            exchange_json = await resp.json()

    # exchange_json = json.dumps(resp, sort_keys=False, indent=4)
    currency_list = []
    exchange_rates = {}
    for currency in currency_list:
        exchange_rates[currency] = exchange_json[currency]["bid"]
    print("Valor convertido: ", exchange_rates)

    converted = exchange_rates.copy()

    for currency, value in converted.items():
        converted[currency] = float(value)
        converted[currency] *= valor

    print("Valor total: ", converted)

    converted = {key: round(converted[key], 2) for key in converted}

    return converted


# exchanges = aiohttp.request(
#     "GET", "https://economia.awesomeapi.com.br/last/BRL-USD,BRL-EUR,BRL-INR"
# )
