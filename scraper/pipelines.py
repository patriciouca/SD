# -*- coding: utf-8 -*-

import csv
from django.utils import timezone



class AmazontrackPipeline(object):
    def process_item(self, item, spider):
        ruta = 'datos/'+"nombre"+'.csv'
        print(ruta)
        #f = open("datosProducto.txt", "a")
        #f.write(item['nombre']+" "+item['precio'])
        #f.close()
        with open(ruta, 'w', newline='') as csvfile:
            fieldnames = ['fecha', 'precio']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'fecha': datetime.datetime.now().time(), 'precio': item['precio']})
        '''
        try:
            #fh = open('/datos/'+item['titulo']+'.csv', 'r')
            #with open('/datos/'+item['titulo']+'.csv', 'a', newline='') as csvfile:
                #fieldnames = ['fecha', 'precio']
                #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #writer.writeheader()
                #writer.writerow({'fecha': timezone.now(), 'precio': item['precio']})
        except FileNotFoundError:
            with open('/datos/'+"nombre"+'.csv', 'w' ,newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'fecha': timezone.now(), 'precio': item['precio']})'''
        return item
