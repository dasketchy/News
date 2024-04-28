from flask import Flask, render_template, request, session, redirect, url_for 
import random
import requests
from src.login import USER_DATABASE
from newsapi import NewsApiClient

import secrets

secret_key = secrets.token_hex(16)  # Generate a 32-character hexadecimal string (16 bytes)

newsapi = NewsApiClient(api_key='25c14ea863dd4ec7996bba717388eca7')

app = Flask(__name__)

app.secret_key = secret_key

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

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)

    if username in USER_DATABASE and USER_DATABASE[username] == password:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return 'Invalid username/password. Please try again.'

    return render_template("index.html")

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home_page'))