"module with functions used in generic tasks"
import json
from pydantic import Json


class Utils:
    "Class that perform generic tasks"

    def transform_input(self, inputs: str | dict[str, str]) -> list[str] | dict | None:
        """Receive a string, extract all hyphens and returns a list with each element that
        is separated by commas. Or receive a dict, extract al "BRL" and return a dict that
        same type.

        Returns:
        list: list of currencies to convert.
        dict: list of currencies converted.
        """
        if isinstance(inputs, str):
            output = inputs.replace("-", "").split(",")
            return output
        if isinstance(inputs, dict):
            new_keys = [key.replace("BRL", "") for key in inputs]
            output = dict(zip(new_keys, inputs.values()))
            return output
        return None

    def fetch_data(
        self, update: bool = False, json_cache: str = "json_file", data: Json = Json
    ) -> Json:
        """Receives a

        Args:
            update (bool, optional): _description_. Defaults to False.
            json_cache (str, optional): _description_. Defaults to "".
            data (dict, optional): _description_. Defaults to {}.

        Returns:
            Any: _description_
        """
        if update:
            json_data = None
        else:
            try:
                with open(json_cache, "r") as file:
                    json_data = json.load(file)
                    print("Fetched data from local cache!")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print("No local cache founds...", ({e}))
                json_data = None

        if not json_data:
            print("Fetching new json data... (Creating local cache)")
            json_data = data
            with open(json_cache, "w", encoding="utf-8") as file:
                json.dump(json_data, file)

        return json_data
