# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LoopnetcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Status = scrapy.Field()
    Price = scrapy.Field()
    Property_Type = scrapy.Field()
    Sub_Type = scrapy.Field()
    Spaces= scrapy.Field()
    Spaces_Available = scrapy.Field()
    Building_Size = scrapy.Field()
    Address = scrapy.Field()
