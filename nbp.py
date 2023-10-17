import requests
import json
from requests.exceptions import HTTPError

def get_rates_of_currency(currency):
    try:
        # Skorzystamy z NBP API
        table = "A"
        rates_number = 12
        url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/last/{rates_number}/"
        response = requests.get(url)
    except HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        if response.status_code == 200:
            return json.dumps(
                response.json(),
                indent=4,
                sort_keys=True), response.json()


if __name__ == '__main__':
    # JSON jako string oraz JSON
    json_caly, GBP = get_rates_of_currency("GBP")
    print(json_caly)
    # Kursy GBP z <rates_number> dni.
    for i in range(len(GBP["rates"])):
        print(f'\nKurs ({i + 1}) GBP: {GBP["rates"][i]["mid"]} z dnia {GBP["rates"][i]["effectiveDate"]}.')
