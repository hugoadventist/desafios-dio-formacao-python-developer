from fastapi import FastAPI
import aiohttp

app = FastAPI()


@app.get("/api/convert/BRL/{valor}")
async def converter_valor(valor: float, moedas: str = "BRL-USD,BRL-EUR,BRL-INR"):
    if moedas:
        moedas += ",BRL-USD,BRL-EUR,BRL-INR"
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://economia.awesomeapi.com.br/last/" + moedas
        ) as resp:
            print(resp.status)
            exchange_json = await resp.json()

    # exchange_json = json.dumps(resp, sort_keys=False, indent=4)
    currency_list = moedas.replace("-", "").split(",")
    print(currency_list)
    exchange_rates = {}
    for currency in currency_list:
        exchange_rates[currency] = exchange_json[currency]["bid"]
    print("Valor convertido: ", exchange_rates)

    converted = exchange_rates.copy()

    for currency in converted:
        converted[currency] = float(converted[currency])
        converted[currency] *= valor

    print("Valor total: ", converted)

    converted = {key: round(converted[key], 2) for key in converted}

    return converted


# exchanges = aiohttp.request(
#     "GET", "https://economia.awesomeapi.com.br/last/BRL-USD,BRL-EUR,BRL-INR"
# )
