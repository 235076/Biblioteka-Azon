import requests


def check_data_types(api_key):
    try:
        response = requests.get("https://api.e-science.pl/api/azon/entry/types/index/",
                                headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.HTTPError as http_err:
        print('http error')
