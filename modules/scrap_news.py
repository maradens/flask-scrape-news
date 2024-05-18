import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    # url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find("body").find_all("h2")
    headlines = []
    for headline in news:
        # print(headline.text.strip())
        headlines.append(headline.text.strip())
    return headlines
