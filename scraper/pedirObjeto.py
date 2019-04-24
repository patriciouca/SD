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

from scraper.items import AmazonItem
from scraper.spiders.amazon import AmazonSpider

lista_nombres = ['Legend-Zelda-Breath-Wild-Nintendo-Switch/dp/B01MS6MO77','YI-1080P60-Dashboard-G-Sensor-Recording/dp/B01C89GCHU','ONeill-Tonal-Camiseta-Manga-Hombre/dp/B07K96RBJ7','SONNENGLAS-Original-micro-USB-Sudáfrica-inoxidable/dp/B00BDPTNB8','+Tira-luz-LED-RGB-compatible/dp/B07MDZ4FFW']

def llamadaArana():
    sys.path.append(os.path.dirname(os.path.abspath('.')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mercado.settings'

    settings_file_path = 'scraper.settings'  # The path seen from root, ie. from main.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

    django.setup()
    spider= AmazonSpider
    item = AmazonItem()
    run_spi_pro(spider)

def otro(spider):
    os.system("scrapy crawl yourspider")

def run_spi_pro(spider):
    def f(q):
        try:
            settings = get_project_settings()
            process = CrawlerProcess(settings)
            start=[]
            '''
            for member in lista_nombres:
                start.append("https://www.amazon.es/"+member)
            '''
            start.append("https://www.amazon.es/Legend-Zelda-Breath-Wild-Nintendo-Switch/dp/B01MS6MO77/ref=br_asw_pdt-4?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=BMEE9DNZEJ7454D8V8A1&pf_rd_t=36701&pf_rd_p=f8585743-c043-4665-80a7-0cc5fe97d596&pf_rd_i=desktop")
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
