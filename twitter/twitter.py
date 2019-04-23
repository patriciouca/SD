import tweepy
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
    print(data)

    #primero ordenar en el csv el ultimo dato al que se hace scrapping, ordenar las filas
    #luego coger la primera fila donde estara el dato mas actualizado

