from datetime import datetime
from typing import Any, Dict, List

ARTICLE_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_article_details(article: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "url": article["url"],
        "title": article["title"],
        "author": article["author"],
        "description": article["description"],
        "image_url": article["urlToImage"],
        "date": str(datetime.strptime(article["publishedAt"], ARTICLE_DATE_FORMAT).date()),
        "time": str(datetime.strptime(article["publishedAt"], ARTICLE_DATE_FORMAT).time()),
    }


# apply filter function, keep only the valid ones
def filter_for_only_valid_articles(articles: List[Dict[str, Any]]) -> filter:
    return filter(filter_valid_article, articles)


# applies a list of functions on a single article
# if we fail any, then we return False to indicate that article is to be filtered away
def filter_valid_article(article: Dict[str, Any]) -> bool:
    # list of functions we want to apply
    filter_functions = [is_removed_article, is_faulty_yahoo_url]

    for filter_function in filter_functions:
        if filter_function(article):
            return False

    return True

def is_removed_article(article: Dict[str, Any]) -> bool:
    return article["content"] == "[Removed]"


def is_faulty_yahoo_url(article: Dict[str, Any]) -> bool:
    return "consent.yahoo" in article["url"]
