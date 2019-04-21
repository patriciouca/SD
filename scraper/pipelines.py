# -*- coding: utf-8 -*-

import csv
from django.utils import timezone



class AmazontrackPipeline(object):
    def process_item(self, item, spider):
        ruta = 'datos/'+item['nombre']+'.csv'
        print(ruta)
        #f = open("datosProducto.txt", "a")
        #f.write(item['nombre']+" "+item['precio'])
        #f.close()

        try:
            fh = open(ruta, 'r')
            with open(ruta, 'a', newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'fecha': timezone.now(), 'precio': item['precio']})

        except FileNotFoundError:
            with open(ruta, 'w' ,newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'fecha': timezone.now(), 'precio': item['precio']})
        return item
