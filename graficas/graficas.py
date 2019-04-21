import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from django.http import HttpResponse
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

def generarGrafica():
    data = pd.read_csv("datos/SONNENGLAS Original, Linterna solar en tarro de vidrio con puerto micro-USB, Comercio justo de Sudáfrica, Vidrio y acero inoxidable, Lámpara Solar Sun Jar.csv", delimiter = ',')
    data.head()
    print(data)

    plt.plot(data['fecha'],data['precio'])
    plt.xlabel('Dia')
    plt.ylabel('Precio')

    plt.savefig('graficas/imagenes/foo.png')
    plt.show()

