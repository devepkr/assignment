# items.py
# Defines the data structure for scraped items

import scrapy

class StubhubsProjectsItem(scrapy.Item):
    title = scrapy.Field()
    datetime = scrapy.Field()
    location = scrapy.Field()
    images = scrapy.Field()