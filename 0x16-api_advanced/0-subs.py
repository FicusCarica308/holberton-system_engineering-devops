#!/usr/bin/python3
""" """
import requests

def number_of_subscribers(subreddit):
    """ """
    subs = requests.get('http://www.reddit.com/r/{}/about'.format(subreddit))
    print(subs.content)
