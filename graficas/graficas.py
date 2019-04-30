import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from dropbox import dropbox

from scraper.dropbox import DescargarDropbox


def generarGrafica():
    dbx = dropbox.Dropbox('c_uLk304JZAAAAAAAAAAGmBbP1ofQmaY52zRtIm7z8_p3NT-1hRwx-ZV3E_DlPeo')
    for entry in dbx.files_list_folder('/datos/').entries:
        print(entry.name)
        DescargarDropbox('/datos/'+entry.name)
        hacerGrafica2("datos.csv",entry.name)
    hacerGrafica2("prueba.csv","prueba.csv")


def hacerGrafica(file,entry):
    data = pd.read_csv("datos/"+file, delimiter=',')
    data.head()
    print(data)

    plt.plot(data['fecha'], data['precio'])
    plt.xlabel('Dia')
    plt.ylabel('Precio')

    plt.savefig('graficas/imagenes/' + entry[:-4] + '.png')
    plt.show()

def hacerGrafica2(file,entry):
    data = pd.read_csv("datos/"+file, delimiter=',')
    data.head()
    print(data)

    print(data['precio'])
    plt.axis([40, 160, 0, 0.03])
    fechas = ['30-04-19 15:04','10-05-19 15:04','12-05-19 15:04']
    valor = ['1,99','2,99','44,99']
    #plt.plot(data['fecha'], data['precio'])
    plt.plot(fechas,valor)
    plt.xlabel('Dia')
    plt.ylabel('Precio')

    plt.savefig('graficas/imagenes/' + entry[:-4] + '.png')
    plt.show()



