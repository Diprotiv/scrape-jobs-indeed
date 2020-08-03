# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    remote = scrapy.Field()
    job_link = scrapy.Field()
    salary = scrapy.Field()
    summary = scrapy.Field()
    date = scrapy.Field()

