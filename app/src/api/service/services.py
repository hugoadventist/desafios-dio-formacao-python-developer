import aiohttp
from cachetools import TTLCache, cached
from ..utils.ETL import Utils

utils = Utils()


class Services:
    """The functions that translate the rules business"""

    @classmethod
    def parser_currencies(cls, currencies="BRL-USD,BRL-EUR,BRL-INR"):
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

    @classmethod
    def extract_json(cls, json_file: dict, coins: list[str] | dict, key: str) -> dict:
        """Extract data of a json file and return a new json

        Returns:
            dict: data with currency exchanges.
        """

        return {currency: json_file[currency][key] for currency in coins}

    @classmethod
    def convert_values(cls, value: float, last_exchange: dict) -> dict:
        """Convert currency values of a json file and return the json with
        desired conversion.

        Returns:
            dict: the values of currencies converted.
        """
        for currency in last_exchange:
            last_exchange[currency] = float(last_exchange[currency])
            last_exchange[currency] *= value
        return {key: round(last_exchange[key], 2) for key in last_exchange}

    @classmethod
    def response(cls, value: float, coins: str, exchange_json: dict) -> dict:
        if coins:
            coins += ",BRL-USD,BRL-EUR,BRL-INR"
        currency_list = utils.transform_input(coins)
        coin_values = cls.extract_json(
            json_file=exchange_json, coins=currency_list, key="bid"  # type: ignore
        ).copy()
        values_converted = utils.transform_input(cls.convert_values(value, coin_values))
        # values_converted = transform_input(cls.convert_values(value, coin_values))

        return values_converted  # type: ignore

    @staticmethod
    @cached(cache=TTLCache(10, ttl=30))
    async def request(url: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, raise_for_status=True) as resp:
                print(resp.status)
                file_json = await resp.json()
        return file_json
