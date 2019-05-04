import logging
from multiprocessing import Process, Queue

from scrapy import signals
import json

import os
import sys
import django
from scrapy.crawler import Crawler, CrawlerProcess, CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from multiprocessing import current_process

from scraper.items import AmazonItem
from scraper.spiders.amazon import AmazonSpider

lista_nombres =[]
def llamadaArana():
    sys.path.append(os.path.dirname(os.path.abspath('.')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mercado.settings'

    settings_file_path = 'scraper.settings'  # The path seen from root, ie. from main.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

    django.setup()
    spider= AmazonSpider
    item = AmazonItem()
    run_spi_pro(spider)

def scrapytareas():
    sys.path.append(os.path.dirname(os.path.abspath('.')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mercado.settings'

    settings_file_path = 'scraper.settings'  # The path seen from root, ie. from main.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

    django.setup()
    spider = AmazonSpider
    item = AmazonItem()
    run_spi_pro_tar(spider)



def otro(spider):
    os.system("scrapy crawl yourspider")


def run_spi_pro_tar(spider):
    def f(q):
        try:
            settings = get_project_settings()
            process = CrawlerProcess(settings)
            start=[]

            start.append("https://www.amazon.es/Bosch-Carton-atornillador-inalámbrico-603-9-a8-006/dp/B01N43TJ8K")
            process.crawl(spider,start_urls=start)
            process.start()  # the script will block here until the crawling is finished
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result



def run_spi_pro(spider):
    def f(q):
        try:
            settings = get_project_settings()
            process = CrawlerProcess(settings)
            start=[]

            for member in lista_nombres:
                start.append("https://www.amazon.es/"+member)

            process.crawl(spider,start_urls=start)
            process.start()  # the script will block here until the crawling is finished
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result
