import os
from twitter_bot_class import Twitter_Bot

if __name__ == "__main__":
    EMAIL = input("Provide your Phone, email or username: ")
    PASSWORD = input("Provide your password: ")
    try:
        tbot = TwitterBot(EMAIL, PASSWORD)
        tbot.login()
        tbot.like_tweets(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)

