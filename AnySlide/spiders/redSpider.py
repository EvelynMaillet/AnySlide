import scrapy
import webbrowser


class RedspiderSpider(scrapy.Spider):
    name = "redSpider"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/Art/"]

    def parse(self, response):
        images = response.css("img").xpath("@src").getall()
        webbrowser.open(images[0])
        pass
