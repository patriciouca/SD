import tweepy
from tweepy import Stream, StreamListener
import pandas as pd
from django.utils import timezone
from unshortenit import UnshortenIt

from lanzamientoTareas.models import Tarea


consumer_key = "hoBOoYlt8LA8lFi5Duc75YQ3Z"
consumer_secret = "D0E8qoQc0cAt5Hw1dwt2vVlbXwUTHRhYHT4eYqe7B7jnv7ZOLH"
access_token = "1105474119980728321-GW24y8vI1PUH2ezm29becgdf30pVXC"
access_token_secret = "lUaxrMUTqDpNS1PyX45HvrGo63ah4SIHZcPQOrfVilf4B"

auth = tweepy.OAuthHandler ( consumer_key , consumer_secret)
auth.set_access_token ( access_token , access_token_secret )
api = tweepy.API (auth)

def escribirTweet(nombre):

    data=pd.read_csv('datos/datos.csv')
    data.head()
    print(data)
    ultimoelemento = len(data['fecha'])-1
    ultimafecha = data['fecha'][ultimoelemento]
    ultimoprecio = data['precio'][ultimoelemento]

    mensajeTweet(ultimafecha,ultimoprecio)


def mensajeTweet(fech,pre,nombre):
    try:
        api.update_status(
            'El producto ' + nombre[0:-4] + ' tiene el siguiente precio a dia ' + fech + '. Precio actualizado: ' + pre)
        api.update_with_media('graficas/imagenes/' + nombre[:-4] + '.png')
    except Exception:
        print("a")

def darMensaje(nombre):
    data = pd.read_csv('datos/datos.csv')
    data.head()
    ultimoelemento = len(data['fecha']) - 1
    ultimafecha = data['fecha'][ultimoelemento]
    ultimoprecio = data['precio'][ultimoelemento]

    mensajeTweet(ultimafecha, ultimoprecio,nombre)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        if("quiero vigilar este producto" in status.text):
            url=status.text[status.text.index("https"):]
            url = url[0:url.index(" ")]

            unshortener = UnshortenIt()
            url = unshortener.unshorten(url)
            print(unshortener.unshorten(url))

            t = Tarea(articulo=url, fecha= timezone.now())
            t.save()


def escuchaMencion():
    print("Escuchando")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["@AmazonCadiz"])

    return 0