#!/usr/bin/python3

#### A tool for turning the Twitter users you have blocked into mutes.

## Users that you unblock will be able to view your profile and message you.
## While muted users will not appear in your feeds.


## This script is...

##    NOT advisable for those who have used the block feature to protect their safety & privacy
##    This script SHOULD be considered by politicians
##    This script SHOULD be used by anyone ordered by a federal judge to unblock twitter users
##    This script SHOULD be used by any representative violating First Amendment rights by preventing constituents from viewing and replying to tweets
##    https://www.nytimes.com/2018/05/23/business/media/trump-twitter-block.html
##    You get the idea, Representatives should do this.



## This script will need to be rerun periodically if you continue to use the block feature.
## When this script was written in June 2018 a total.

#### Import dependencies
import json
import tweepy
import re
import random
import sys
import timeit
import time

#### Define variables
start = timeit.default_timer()
exception_title = 'exceptions'
counter = 0

def get_api_keys():
    #### Set Twitter API key dictionary
    try:    #### Attempt to load API keys file
        keys_json = json.load(open('/usr/local/keys.json'))
        #### Specify key dictionary wanted (generally [Platform][User][API])
        Keys = keys_json["Twitter"]["ClimateCong_Bot"]["ClimatePolitics"]
        #Keys = keys_json["Twitter"]["AGreenDCBike"]["HearHerVoice"]
    except Exception as e:
        er = e
        if er.errno == 2: #File not found enter key dictionary values manually
            print("\nNo twitter API key was found in /usr/local/keys.json\n",
                 "Acquire an API key at https://apps.twitter.com/\n",
                 "to supply key manually press Enter\n")
            Keys = {}
            Keys['Consumer Key (API Key)'] = input('Enter the Twitter API Consumer Key\n')
            Keys['Consumer Secret (API Secret)'] = input('Enter the Twitter API Consumer Secret Key\n')
            Keys['Access Token'] = input('Enter the Twitter API Access Token\n')
            Keys['Access Token Secret'] = input('Enter the Twitter API Access Token Secret\n')
            Keys['Owner'] = input('Enter your Twitter username associated with the API keys\n')
        else:
            print(e)
    return(Keys)

#### Get keys
Keys = get_api_keys()

#### Access Twitter API using Tweepy & key dictionary definitions
auth = tweepy.OAuthHandler( Keys['Consumer Key (API Key)'], Keys['Consumer Secret (API Secret)'] )
auth.set_access_token( Keys['Access Token'], Keys['Access Token Secret'] )
api = tweepy.API(auth)
user = api.auth.get_username()



#### Returns a human readable time difference
def calc_time():
    # Stop the timer
    stop = timeit.default_timer()
    total_time = stop - start
    # Formate running time.
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    timed = str("%d:%d:%d" % (hours, mins, secs))
    return (timed)

#### Increases counter and prints progress
def add_2_counter(counter):
    counter += 1
    if counter % 100 == 0:
        timed = calc_time()
        print("Time elapsed:", timed, " Users blocked:", str(counter))
    else:
        print(counter, end='\r')
        pass
    return (counter)

#### Fetch users that have been blocked
def get_blocked_list():
    blocks = api.blocks()
    return(blocks)




####
### Tweepy users have made requests for support of mute & unmute:
##     https://github.com/tweepy/tweepy/issues/528
##     https://github.com/tweepy/tweepy/issues/919
### Responding to these requests and my own needs
### a branch with mute & unmute ability has been submitted for tweepy admin approval:
##     https://github.com/tweepy/tweepy/pull/1055/commits
####

def block2mute(one_user):
    print(one_user.screen_name, "\t", one_user.id, "\t",
          "Blocked:", one_user.blocking,
          " Muting:", one_user.muting)
    try:
        api.create_mute(one_user.id, monitor_rate_limit=True, wait_on_rate_limit=True)
        print("Muted")
        api.destroy_block(one_user.id, monitor_rate_limit=True, wait_on_rate_limit=True)
        print("Unblocked")
    except Exception as e:
        er = e
        if e.api_code == 160:
            print("Private account")
        if e.api_code == 50:
            print("User not found", str(one_user.screen_name))
        if e.api_code == 88:
            print("Rate limit exceeded")
            time.sleep(15*60)
        else:
            print("api ERROR")
            print(e)
            time.sleep(3 * 60 * 60)



#### Work flow
blocks = get_blocked_list()

while len(blocks) > 0:
    print("New Blocks list count is:", len(blocks))
    for one_user in blocks:
        block2mute(one_user)
        counter = add_2_counter(counter)
    blocks = get_blocked_list()

###################################################################
#  Do not use any of the code I have written with harmful intent. #
#                                                                 #
#    By using this code you accept that everyone has the          #
#       right to choose their own gender identity.                #
###################################################################

