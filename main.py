import json
import requests
import os
from utils.fetch_news import fetch_news


with open("config/keywords.json") as f:
    data = json.load(f)

keywords = data["keywords"]

fetch_news(keywords)    