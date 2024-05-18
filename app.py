import time

from flask import Flask, render_template, request

import modules.scrap_news as scrap_news

app = Flask(__name__)


@app.route("/")
def home():
    headlines = scrap_news.scrape_news()
    return render_template("index.html", headlines=headlines)


@app.route("/bbc")
def bbc_news():
    url = "https://www.bbc.com/news"
    headlines = scrap_news.scrape_news(url)
    return render_template("index.html", headlines=headlines)


@app.route("/kompas")
def kompas_news():
    url = "https://www.kompas.com"
    headlines = scrap_news.scrape_news(url)
    return render_template("index.html", headlines=headlines)


@app.route("/detik")
def detik_news():
    url = "https://www.detik.com"
    headlines = scrap_news.scrape_news(url)
    return render_template("index.html", headlines=headlines)


@app.route("/long/<newspage>")
def news_page(newspage):
    if newspage != "bbc":
        url = "https://www." + newspage + ".com"
    else:
        url = "https://www." + newspage + ".com/news"

    # print(url)

    # headlines = scrap_news.scrape_news(url)
    # return render_template("index.html", headlines=headlines)
    return render_template("loading.html", my_data=url)


@app.route("/processing")
def processing():
    # This is where the time-consuming process can be.
    data = "No data was passed"
    # In this case, the data was passed as a get request as you can see at the bottom of the loading.html file
    if request.args.to_dict(flat=False)["data"][0]:
        data = str(request.args.to_dict(flat=False)["data"][0])
    # This is where your time-consuming stuff can take place (sql queries, checking other apis, etc)
    headlines = scrap_news.scrape_news(data)
    time.sleep(
        10
    )  # To simulate something time-consuming, I've tested up to 100 seconds
    # You can return a success/fail page here or whatever logic you want
    return render_template("result.html", headlines=headlines)


if __name__ == "__main__":
    app.run(debug=True)

# next coba bikin router untuk pilih portal yang mau di scrap..misalnya bbc kompas detik
