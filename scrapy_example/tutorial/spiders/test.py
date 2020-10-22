import scrapy
from scrapy import cmdline


class QuotesSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                "author": quote.xpath("child::span/small[@class='author']/text()").get(),
                "text": quote.xpath("child::span[@class='text']/text()").get(),
                "tags": quote.xpath("child::div/a[@class='tag']/text()").getall(),
                "next_url": response.xpath("//li[@class='next']/a/@href").get(),
            }
            # next_page_url = 'http://quotes.toscrape.com' + response.xpath("//li[@class='next']/a/@href").get()
            #
            # if next_page_url is not None:
            #     yield response.follow(next_page_url, callback=self.parse)

            # next_url = 'http://quotes.toscrape.com' + response.xpath("//li[@class='next']/a/@href").get()
            # yield response.follow(next_url, callback=self.parse)

            # next_url = response.xpath("//li[@class='next']/a/@href").get()
            # if next_url is not None:
            #     yield response.follow(next_url, callback=self.parse)

            # yield from response.follow_all(response.xpath("//li[@class='next']/a/@href"), callback=self.parse)

            yield from response.follow_all(xpath="//li[@class='next']/a/@href", callback=self.parse)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl test".split())
