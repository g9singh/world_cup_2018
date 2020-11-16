# import modules
import twint
import pandas as pd

fans_df = pd.read_csv("results.csv")
for username in fans_df.username:
    c = twint.Config()
    c.Search = "worldcup OR worldcup2018"
    c.Store_csv = True
    c.Since = "2016-06-15"
    c.Until = "2020-11-15"
    c.Pandas = True
    c.Username = username
    c.Limit = 10000
    twint.run.Search(c)

    Tweets_df = twint.storage.panda.Tweets_df
    print(Tweets_df)
    Tweets_df.to_csv('user_tweets/' + username + '.csv')
    print('Scraping has completed!')



