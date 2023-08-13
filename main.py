from scrapy import cmdline


def main():
    cmdline.execute(["scrapy", "crawl", "redSpider"])
    
if __name__ == '__main__':
	main()