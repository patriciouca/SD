# -*- coding: utf-8 -*-
import scrapy

try:
    from items import AmazonItem
except ImportError:
    from scraper.items import AmazonItem

class AmazonSpider(scrapy.Spider):


    name = 'amazon'
    allowed_domains = ['amazon.com']


    def parse(self, response):

        ml_item = AmazonItem()

        titulo = response.xpath('//span[@id="productTitle"]/text()').get()
        titulo= titulo.rstrip().lstrip()
        precio = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
        precio=precio.replace('EUR', "", )
        print(titulo)
        print(precio)
        ml_item['nombre'] = titulo
        ml_item['precio'] = precio
        return ml_item
