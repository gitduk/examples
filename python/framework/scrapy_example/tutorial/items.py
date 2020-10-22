# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    H1 = scrapy.Field()
    H2 = scrapy.Field()
    H3 = scrapy.Field()
    pass
