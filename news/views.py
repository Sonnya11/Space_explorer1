from django.shortcuts import render
import requests

def latest_news(request):
    # Spaceflight News API
    url = "https://api.spaceflightnewsapi.net/v4/articles/"
    response = requests.get(url)
    data = response.json()

    # Extract only required fields
    articles = []
    for item in data.get("results", []):
        articles.append({
            "title": item.get("title"),
            "summary": item.get("summary"),
            "url": item.get("url"),
            "image_url": item.get("image_url"),
        })

    return render(request, "news/latest_news.html", {"news_list": articles})
