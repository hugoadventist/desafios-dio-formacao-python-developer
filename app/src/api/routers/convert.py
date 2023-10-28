"""Returns the HTTP requests

Returns:
    dict: the json file with values converted.
"""
from typing import Annotated
from fastapi import APIRouter
from fastapi import Path, Query
from ..service.services import Services
from ..utils.ETL import Utils

router = APIRouter()

services = Services()

utils = Utils()


@router.get("/api/convert/BRL/{value}", status_code=200)
async def read_value(
    value: Annotated[float, Path(title="The value in R$ to convert.", gt=0)],
    coins: Annotated[
        str, Query(title="The coins desired to convert.")
    ] = "BRL-USD,BRL-EUR,BRL-INR",
) -> dict:
    """Receive the path parameter and default to query parameter containing
    "BRL-USD,BRL-EUR,BRL-INR".

    Args:
        valor (float): Value in R$ to convert.
        coins (str, optional): the query parameter with desired currencies.
        Defaults to "BRL-USD,BRL-EUR,BRL-INR".

    Returns:
        dict: the json file with currency conversion done.
    """
    # async with session.get(
    #     "https://economia.awesomeapi.com.br/last/" + coins, raise_for_status=True
    # ) as resp:
    #     print(resp.status)
    #     exchange_json = await resp.json()
    # url = f"https://economia.awesomeapi.com.br/last/ + {coins}"

    exchange_json = await services.request(
        f"https://economia.awesomeapi.com.br/last/{coins}"
    )

    # result = services.response(value, coins, exchange_json)

    created_json_file = utils.fetch_data(
        update=True, json_cache="exchanged_rates.json", data=exchange_json
    )

    # print(created_json_file)

    # print(type(created_json_file.values.__name__))

    return services.response(value, coins, exchange_json)
