import os
from twitter_bot_class import Twitter_Bot
"""
Automatically likes the tweets in your feed
"""
if __name__ == "__main__":
    EMAIL = input("Provide your Phone, email or username: ")
    PASSWORD = input("Provide your password: ")
    try:
        tbot = Twitter_Bot(EMAIL, PASSWORD)
        tbot.login()
        tbot.like_tweets(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)

