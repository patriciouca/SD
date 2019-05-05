from scraper.twitter import escuchaMencion
from background_task import background



@background(schedule=1)
def escucharTweets():
    escuchaMencion()