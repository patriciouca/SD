# -*- coding: utf-8 -*-

import csv
import calendar

from django.utils import timezone
from datetime import datetime

from scraper.dropbox import SubirDropbox, DescargarDropbox


class AmazontrackPipeline(object):

    def process_item(self, item, spider):
        titulo = 'datos' + '.csv'
        ruta = 'datos/' + titulo

        tituloH=item['nombre'][0:50]+'.csv'

        formato2 = "%d-%m-%y %H:%m"
        hoy = datetime.today()
        fecha = hoy.strftime(formato2)

        if DescargarDropbox('/datos/'+tituloH) == 0:
            print("No existe")
            with open(ruta, 'w', newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'fecha': fecha, 'precio': item['precio']})
        else:
            print("Ya existe")
            with open(ruta, 'a', newline='') as csvfile:
                fieldnames = ['fecha', 'precio']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'fecha': fecha, 'precio': item['precio']})

        SubirDropbox(tituloH)

        return item