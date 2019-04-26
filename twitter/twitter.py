import tweepy
from tweepy import Stream, StreamListener
import pandas as pd

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

    mensajeTweet(ultimoelemento,ultimafecha,ultimoprecio)


def mensajeTweet(elem,fech,pre):

    api.update_status('El producto Camiseta tiene el siguiente precio a dia ' + fech + '. Precio actualizado: ' + pre)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        f = open('holamundo.txt', 'w')
        f.write(status.text)
        f.close()


def escuchaMencion():
    print("Escuchando")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["@AmazonCadiz"])

    return 0;




