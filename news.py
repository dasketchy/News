from flask import Flask, render_template, request
import random
import requests
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

    url_title_list = [
        {"url": response["articles"][0]["url"], "title": response["articles"][0]["title"]},
        {"url": response["articles"][1]["url"], "title": response["articles"][1]["title"]},
        {"url": response["articles"][2]["url"], "title": response["articles"][2]["title"]}
    ]

    return render_template("results.html", url_title_list=url_title_list, query=query)



@app.route("/login")
def login_page():

    return render_template("page.html")
