import requests
import json

def fetch_market_news():
    """
    Fetches the latest market news titles from Seeking Alpha via RapidAPI.
    
    Returns:
        str: A formatted string containing numbered news titles.
    """
    url = "https://seeking-alpha.p.rapidapi.com/news/v2/list"
    querystring = {"size": "20", "category": "market-news::all", "number": "1"}
    headers = {
        "x-rapidapi-key": "<API_KEY>",
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get("data", [])

    all_news = ""
    for i, item in enumerate(data, start=1):
        title = item.get("attributes", {}).get("title")
        if title:
            all_news += f"{i}. {title}\n"

    return all_news

def get_global_quote(symbol: str) -> str:
    """
    Fetches the global quote for a given stock symbol using Alpha Vantage API.

    Args:
        symbol (str): The stock symbol to query (e.g., "MSFT").

    Returns:
        str: The 'Global Quote' section of the API response as a formatted string.
    """
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "datatype": "json"
    }
    headers = {
        "x-rapidapi-key": "<API_KEY>",
        "x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    return json.dumps(data.get("Global Quote", {}), indent=2)

if __name__ == "__main__":
    print(get_global_quote("MSFT"))