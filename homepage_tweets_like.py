import os
from twitter_bot_class import Twitter_Bot
#this code takes the input of email and password from the user and sends the values to the Twitter_Bot function
if __name__ == "__main__":
    #Taking input of email and password from the user
    EMAIL = input("Provide your Phone, email or username: ") 
    PASSWORD = input("Provide your password: ")
    try:
        #calling the function Twitter_Bot and passing the the values of EMAIL and PASSWORD
        tbot = Twitter_Bot(EMAIL, PASSWORD) 
        tbot.login()
        tbot.like_tweets(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)

