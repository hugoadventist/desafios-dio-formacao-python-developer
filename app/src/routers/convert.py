"""Returns the HTTP requests

Returns:
    dict: the json file with values converted.
"""
import aiohttp
from main import app
from ..service.services import request


@app.get("/api/convert/BRL/{value}", status_code=200)
async def read_value(value: float, coins: str = "BRL-USD,BRL-EUR,BRL-INR") -> dict:
    """Receive the path parameter and default to query parameter containing
    "BRL-USD,BRL-EUR,BRL-INR".

    Args:
        valor (float): Value in R$ to convert.
        moedas (str, optional): the query parameter with desired currencies.
        Defaults to "BRL-USD,BRL-EUR,BRL-INR".

    Returns:
        dict: the json file with currency conversion done.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://economia.awesomeapi.com.br/last/" + coins, raise_for_status=True
        ) as resp:
            print(resp.status)
            exchange_json = await resp.json()

    return request(value, coins, exchange_json)
