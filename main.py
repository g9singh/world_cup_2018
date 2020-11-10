# import modules
import pandas as pd
import tweepy


# function to display data of each tweet
def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")
    print(f"Created at:{ith_tweet[9]}")

def checkForHashtag(tweet):

    if 'worldcup2018' in tweet[8]:
        print('contains hashtag')


# function to perform data extraction
def scrape(words, form_date, to_date, numtweet):
    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'description', 'location', 'following',
                               'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags', 'created_at'])

    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_full_archive, query=words,
                           fromDate=from_date, toDate=to_date, environment_name="dev").items(numtweet)

    # .Cursor() returns an iterable object. Each item in
    # the iterator has various attributes that you can access to
    # get information about each tweet
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        created_at = tweet.created_at

        text = tweet.text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext, created_at]
        db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        checkForHashtag(ith_tweet)
        i = i + 1
    filename = 'scraped_tweets.csv'

    # we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == '__main__':
    # Enter your own credentials obtained
    # from your developer account
    consumer_key = "fKqrUWh5n5ndQRXZRJSO8uitf"
    consumer_secret = "jBhllJ7UocplVQagryjd0kx7myrV7SzOmWK7OyXFSgtfGkLDqv"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)


    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search for")
    # words = input()
    words = "FRA"
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    # date_since = input()
    from_date = "201709200000"
    to_date = "201709300000"
    # number of tweets you want to extract in one run
    numtweet = 100
    scrape(words, from_date, to_date, numtweet)
    print('Scraping has completed!')

