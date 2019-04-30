import tweepy
from tweepy import Stream, StreamListener
import pandas as pd
from django.utils import timezone

from lanzamientoTareas.models import Tarea

consumer_key = "hoBOoYlt8LA8lFi5Duc75YQ3Z"
consumer_secret = "D0E8qoQc0cAt5Hw1dwt2vVlbXwUTHRhYHT4eYqe7B7jnv7ZOLH"
access_token = "1105474119980728321-GW24y8vI1PUH2ezm29becgdf30pVXC"
access_token_secret = "lUaxrMUTqDpNS1PyX45HvrGo63ah4SIHZcPQOrfVilf4B"

auth = tweepy.OAuthHandler ( consumer_key , consumer_secret)
auth.set_access_token ( access_token , access_token_secret )
api = tweepy.API (auth)

def escribirTweet():

    data=pd.read_csv('datos/O\'Neill LM Tonal Camiseta Manga Corta, Hombre.csv')
    data.head()
    ultimoelemento = len(data['fecha'])-1
    ultimafecha = data['fecha'][ultimoelemento]
    ultimoprecio = data['precio'][ultimoelemento]

    mensajeTweet(ultimafecha,ultimoprecio)


def mensajeTweet(fech,pre):

    from lanzamientoTareas.models import Tarea
    for member in Tarea.objects.all():
        api.update_status('El producto ' + member.articulo +' tiene el siguiente precio a dia ' + fech + '. Precio actualizado: ' + pre)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        if("quiero vigilar este producto" in status.text):
            url=status.text[status.text.index("https"):]
            url = url[0:url.index(" ")]
            t = Tarea(articulo=url, fecha= timezone.now())
            t.save()


def escuchaMencion():
    print("Escuchando")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["@AmazonCadiz"])

    return 0




