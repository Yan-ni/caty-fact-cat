import requests
from utils import config

global_settings = config.get_settings()


def get_fact() -> str:
    """Requests a cat fact from cat fact API and returns the fact concatenated with "Did you know ! " at the start of the fact."""

    try:
        response = requests.get(global_settings.cat_fact_api_url)
        response.raise_for_status()
        response_json = response.json()
    except Exception:
        return None

    response_data = response_json.get("data")

    if response_data is None:
        return None

    cat_fact = response_data[0]

    return cat_fact
