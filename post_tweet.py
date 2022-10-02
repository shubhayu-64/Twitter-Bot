import os
from twitter_bot_class import Twitter_Bot
"""
Tweets so the world can see it
"""

if __name__ == "__main__":
    try:
        EMAIL = input("Provide your Phone, email or username: ")
        PASSWORD = input("Provide your password: ")
        tbot = Twitter_Bot(EMAIL, PASSWORD)
        tbot.login()
        tbot.post_tweets("My bot's first tweet!")
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)
