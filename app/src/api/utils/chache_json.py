import json


def fetch_data(*, update: bool = False, json_cache: str, data: dict):
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
