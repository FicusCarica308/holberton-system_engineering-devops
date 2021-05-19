#!/usr/bin/python3
"""Module contains singular function"""
import requests
import json


def number_of_subscribers(subreddit):
    """Finds the amount of subscribers from a given subreddit"""
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'MannyAgent',
        }
    )
    subs_resp = requests.get('https://www.reddit.com/r/{}/about.json'.
                        format(subreddit))
    if subs_resp.reason != 'OK':
        return 0
    resp = subs_resp.json()
    try:
        subs = resp['data']['subscribers']
    except:
        return 0
