import requests


class FXAPI:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.apilayer.com/exchangerates_data/latest",
    ):
        """
        FXAPI instance for APIs that require an access key.

        Args:
            api_key (str): Your API key from apilayer or similar.
            base_url (str): Base URL of the FX API endpoint.
        """
        self.api_key = api_key
        self.base_url = base_url

    def fetch_rates(self, base="USD", symbols=None, amount=1.0):
        """
        Fetch live FX rates from the API.

        Args:
            base (str): Base currency.
            symbols (list[str] | str | None): List of target currencies or comma-separated string.
            amount (float): Convert specific amount.

        Returns:
            dict: Dictionary of rates or converted amounts.
        """
        headers = {"apikey": self.api_key}
        params = {"base": base}

        if symbols:
            if isinstance(symbols, list):
                params["symbols"] = ",".join(symbols)
            else:
                params["symbols"] = symbols

        try:
            response = requests.get(
                self.base_url, headers=headers, params=params, timeout=10
            )
            response.raise_for_status()
            data = response.json()

            if not data.get("success", False):
                raise ValueError(
                    f"API error: {data.get('error', {}).get('info', 'Unknown error')}"
                )

            rates = data.get("rates", {})
            # Multiply by amount if needed
            for k in rates:
                rates[k] = rates[k] * amount

            return rates

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

        except Exception as e:
            print(f"Error: {e}")
            return {}


def get_crypto_price(ids=["bitcoin", "ethereum"], vs_currencies=["usd"]):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(ids), "vs_currencies": ",".join(vs_currencies)}
    resp = requests.get(url, params=params)
    return resp.json()


# Example usage
prices = get_crypto_price()
print(prices)
# Output: {'bitcoin': {'usd': 29384}, 'ethereum': {'usd': 1900}}
