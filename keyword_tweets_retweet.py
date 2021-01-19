import os
from twitter_bot_class import Twitter_Bot

if __name__ == "__main__":
    try:
        EMAIL = input("Provide your Phone, email or username: ")
        PASSWORD = input("Provide your password: ")
        tbot = Twitter_Bot(EMAIL,PASSWORD)
        tbot.login()
        tbot.search('100DaysOfCode')
        tbot.retweet(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)
