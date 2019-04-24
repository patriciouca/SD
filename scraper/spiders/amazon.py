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
        precio = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
        titulo= titulo.rstrip().lstrip()
        if not precio:
            precio = response.xpath('//span[@class="a-color-price"]/text()').get()

        precio = str(precio)
        if "EUR" in precio:
            precio=precio.replace('EUR', "", )
        if "$" in precio:
            precio = precio.replace('$', "", )
        print(titulo)
        print(precio)
        ml_item['nombre'] = titulo
        ml_item['precio'] = precio
        return ml_item
