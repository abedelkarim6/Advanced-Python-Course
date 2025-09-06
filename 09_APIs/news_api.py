# https://newsapi.org/account
import os
import dotenv
import requests

dotenv.load_dotenv()

news_api = os.getenv("NEWS_API")


def get_news(query="technology", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "pageSize": page_size, "apiKey": news_api}
    resp = requests.get(url, params=params)
    return resp.json()["articles"]


if __name__ == "__main__":
    # Example usage
    articles = get_news()
    for art in articles:
        print(art["title"], "-", art["source"]["name"])
