"""The functions that translate the rules business"""
import aiohttp


def parser_currencies(currencies="BRL-USD,BRL-EUR,BRL-INR"):
    """Raise an error if the instance not is str

    Args:
        currencies (str, optional): the . Defaults to "BRL-USD,BRL-EUR,BRL-INR".

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(currencies, str):
        raise TypeError("Favor inserir uma lista com os parâmetros válidos!")
    return currencies


def transform_input(entradas: str | dict) -> list | dict:
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


def extract_json(json_file: dict, coins: list, key: str) -> dict:
    """Extract data of a json file and return a new json

    Returns:
        dict: data with currency exchanges.
    """

    return {currency: json_file[currency][key] for currency in coins}


def convert_values(value: float, last_exchange: dict) -> dict:
    """Convert currency values of a json file and return the json with
    desired conversion.

    Returns:
        dict: the values of currencies converted.
    """
    for currency in last_exchange:
        last_exchange[currency] = float(last_exchange[currency])
        last_exchange[currency] *= value
    return {key: round(last_exchange[key], 2) for key in last_exchange}


def request(value: float, coins: str, exchange_json: dict) -> dict:
    if coins:
        coins += ",BRL-USD,BRL-EUR,BRL-INR"
    currency_list = transform_input(coins)
    coin_values = extract_json(
        json_file=exchange_json, coins=currency_list, key="bid"
    ).copy()
    values_converted = transform_input(convert_values(value, coin_values))

    return values_converted
