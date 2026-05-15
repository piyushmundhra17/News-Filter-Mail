import json
import dotenv
import requests
import os

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")


with open("config/keywords.json") as f:
    data = json.load(f)

keywords = data["keywords"]

def fetch_news(keywords):
    url = "https://newsdata.io/api/1/market"
    for keyword in keywords:
        params={
            "apikey": API_KEY,
            "q": keyword,
            "language": "en",
            "country": "in"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            news = response.json()
        else:
            print(f"Error{response.status_code}: {response.text}")
        data=response.json()
        articles=data.get("results",[])
        if not articles:
            print("No news Found")
            continue
        for article in articles:
            title=article.get("title")
            link=article.get("link")
            description=article.get("description")
            print(f"Title: {title}\nLink: {link}\nDescription: {description}\n\n")    

fetch_news(keywords)    