from flask import Flask, render_template, request
from newsapi import NewsApiClient

from util import filter_for_only_valid_articles, get_article_details

newsapi = NewsApiClient(api_key="25c14ea863dd4ec7996bba717388eca7")

app = Flask(__name__)


@app.route("/")
def home_page() -> None:
    response = newsapi.get_top_headlines(language="en")

    # Show either first 10 articles, or all articles if total number of articles is less than 10
    article_list = [get_article_details(response["articles"][i]) for i in range(min(10, len(response["articles"])))]

    return render_template("index.html", article_list=article_list)


@app.route("/search_articles", methods=["POST"])
def search_articles() -> None:
    query = request.form["query"]

    response = newsapi.get_everything(language="en", q=query)

    articles = filter_for_only_valid_articles(response["articles"])

    article_list = [get_article_details(article) for article in articles]

    return render_template("results.html", article_list=article_list, query=query)


@app.route("/login")
def login_page() -> None:
    return render_template("page.html")
