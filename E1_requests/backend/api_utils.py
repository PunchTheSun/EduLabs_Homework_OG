import requests
import climage


def get_nationalize_data(request_name: str):
    response = requests.get("https://api.nationalize.io/", params={'name': request_name})
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError


def get_countryrest_data(country_code: str):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
    if response.status_code == 200:
        return response.json()
