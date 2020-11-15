import twint


# arguments: list_of_world_cup_tweeters should be a list of pandas data frame that contains tweets and usernames
#            max_num_of_followers is the number of followers to query per user
# returns a list of "true" fans (users who follow a team and the @FIFAWorldCup)
def get_true_fans(list_of_world_cup_tweeters, max_num_of_followers):
    list_of_world_cup_tweeters['following'] = [[] for x in list_of_world_cup_tweeters['username']]
    list_of_world_cup_tweeters['fan'] = [False for x in list_of_world_cup_tweeters['username']]
    list_of_teams = ["Arsenal", "AVFCofficial", "OneRovers", "officialBWFC", "ChelseaFC", "YourEverton",
                     "Fulham FC",
                     "LFC", "MCFC", "NUFCofficial", "NorwichCityFC", "officialQPR", "officialSCFC",
                     "SAFCofficial",
                     "SpursOfficial", "WBAFCofficial", "LaticsOfficial", "OfficialWolves"]
    world_cup_tag = set(['FIFAWorldCup', 'FIFA'])
    set_of_teams = set(list_of_teams)
    i = 0
    for user in list_of_world_cup_tweeters.username:
        c = twint.Config()
        c.Username = user
        c.Pandas = True
        c.Limit = max_num_of_followers
        twint.run.Following(c)

        following_df = twint.storage.panda.Follow_df
        if "following" in following_df.columns:
            print('on iteration ' + str(i) + ' of ' + str(len(list_of_world_cup_tweeters.username)))
            list_of_following = following_df['following'][user]
            print(list_of_world_cup_tweeters)
            print("user is " + user)
            print(list_of_following)
            if set(list_of_following) & set_of_teams & world_cup_tag:
                list_of_world_cup_tweeters.at[list_of_world_cup_tweeters['username'] == user, 'fan'] = True

            else:
                list_of_world_cup_tweeters.at[list_of_world_cup_tweeters['username'] == user, 'fan'] = False

            list_of_world_cup_tweeters.at[list_of_world_cup_tweeters['username'] == user, 'following'] = ', '.join(list_of_following)
        i = i + 1
    return list_of_world_cup_tweeters

#
# # this function grabs 100 users who follow FIFAWorldCup
# def get_wc_followers():
#     c = twint.Config()
#     c.Username = "FIFAWorldCup"
#     c.Pandas = True
#     c.Limit = 100
#     twint.run.Followers(c)
#
#     followers_df = twint.storage.panda.Follow_df
#     if "followers" in followers_df.columns:
#         list_of_followers = followers_df['followers']['FIFAWorldCup']
#         print(len(list_of_followers))
#         return list_of_followers
#     return []

# list_of_WC_Followers = get_wc_followers()
# list_of_true_fans = get_true_fans(list_of_WC_Followers)
# print(list_of_true_fans)
# list_of_true_fans.to_csv("fans.csv")
