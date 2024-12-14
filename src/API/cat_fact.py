import requests


class CatFact:
    @staticmethod
    def get_fact() -> str:
        """Requests a cat fact from cat fact API and returns the fact concatenated with "Did you know ! " at the start of the fact."""
        api_url_cat_fact = f"https://meowfacts.herokuapp.com/"

        try:
            response = requests.get(api_url_cat_fact)
            response.raise_for_status()
            response_json = response.json()
        except:
            return None

        response_data = response_json.get("data")

        if response_data is None:
            return None

        cat_fact = response_data[0]

        return cat_fact
