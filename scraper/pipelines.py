# -*- coding: utf-8 -*-

import csv
from datetime import datetime, date, time, timedelta
import calendar

from django.utils import timezone
from dropbox import dropbox

from scraper.dropbox import SubirDropbox, DescargarDropbox


class AmazontrackPipeline(object):

    '''
    def process_item(self, item, spider):
        titulo=item['nombre'][0:10]+'.csv'
        ruta = 'datos/'+titulo

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
    '''


    def process_item(self, item, spider):
        titulo = 'datos' + '.csv'
        ruta = 'datos/' + titulo

        tituloH=item['nombre'][0:10]+'.csv'

        formato2 = "%d-%m-%y %H:%m"
        hoy = datetime.today()  # Asigna fecha-hora
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