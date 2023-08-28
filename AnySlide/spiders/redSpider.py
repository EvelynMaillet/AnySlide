import scrapy
import webbrowser
import time


class RedspiderSpider(scrapy.Spider):
    name = "redSpider"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/Art/"]

    def parse(self, response):
        images = list(set(response.css("img").xpath("@src").getall()))
        print(images)
        webbrowser.open(images[2])
        pass
