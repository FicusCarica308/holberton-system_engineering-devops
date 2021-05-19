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
    subs = requests.get('https://www.reddit.com/r/{}/about.json'.
                        format(subreddit))
    if subs.reason != 'OK':
        return (0)
    resp = subs.json()
    if 'data' in resp:
        return (subs.json()['data']['subscribers'])
    else:
        return (0)
