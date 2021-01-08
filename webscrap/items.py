# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    last = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    chg = scrapy.Field()
    chgper = scrapy.Field()
    volume = scrapy.Field()
    pass
