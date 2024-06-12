from flask import Flask, render_template, request
import random
import requests
from datetime import datetime
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='25c14ea863dd4ec7996bba717388eca7')

app = Flask(__name__)

@app.route("/")
def home_page():
    response = newsapi.get_top_headlines(language='en')
    print(response)

    url_title_list = [
        {"url": response["articles"][0]["url"], "title": response["articles"][0]["title"]},
        {"url": response["articles"][1]["url"], "title": response["articles"][1]["title"]},
        {"url": response["articles"][2]["url"], "title": response["articles"][2]["title"]}
    ]
    
    return render_template("index.html", url_title_list=url_title_list)

@app.route("/search_articles", methods=['POST'])
def search_articles():
    query = request.form["query"]
    print(query)

    response = newsapi.get_everything(language='en', q=query)
    print(response)

    """
    {'source': {'id': None, 'name': 'BBC News'}, 
    'author': 'BBC Sport', 
    'title': "Real Madrid crowned champions after Barca's defeat at Girona", 
    'description': 'Real Madrid crowned champions of La Liga for the 36th time after Barcelona lose against Girona.', 
    'url': 'https://www.bbc.com/sport/football/articles/c0x05j54l8wo', 
    'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_sport/e408/live/d555ab30-0a44-11ef-a26b-0541326d66ca.jpg', 
    'publishedAt': '2024-05-04T18:42:17Z', 
    'content': "Real Madrid were crowned champions of La Liga for the 36th time after Barcelona suffered a 4-2 defeat by Girona.\r\nCarlo Ancelotti's side eased to a 3-0 win over Cadiz earlier on Saturday which meant … [+712 chars]"}
    """

    # Define the format
    date_format = "%Y-%m-%dT%H:%M:%SZ"

    url_title_list = [
        {
            "url": article["url"], 
            "title": article["title"],
            "author": article["author"],
            "description": article["description"],
            "image_url": article["urlToImage"],
            "date": str(datetime.strptime(article["publishedAt"], date_format).date()),
            "time": str(datetime.strptime(article["publishedAt"], date_format).time()),
        } 
        for article in response["articles"]
    ]

    return render_template("results.html", url_title_list=url_title_list, query=query)



@app.route("/login")
def login_page():

    return render_template("page.html")
