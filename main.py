# import modules
import twint
import get_list_of_fans

c = twint.Config()
c.Limit = 1000
c.Search = "worldcup OR worldcup2018"
c.Store_csv = True
c.Since = "2018-06-15"
c.Until = "2018-07-16"
c.Pandas = True
twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
max_num_of_followers = 300
true_fans = get_list_of_fans.get_true_fans(Tweets_df, max_num_of_followers)
print(true_fans)
true_fans.to_csv('results.csv')
print('Scraping has completed!')



