# -*- coding: utf-8 -*-

import csv
from datetime import datetime, date, time, timedelta
import calendar

from django.utils import timezone



class AmazontrackPipeline(object):
    def process_item(self, item, spider):
        ruta = 'datos/'+item['nombre']+'.csv'

        formato2 = "%d-%m-%y %H:%m"
        hoy = datetime.today()  # Asigna fecha-hora
        fecha = hoy.strftime(formato2)
        print(fecha)

        try:
            fh = open(ruta, 'r')
            with open(ruta, 'a', newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'fecha': fecha, 'precio': item['precio']})

        except FileNotFoundError:
            with open(ruta, 'w' ,newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'fecha': fecha, 'precio': item['precio']})
        return item
