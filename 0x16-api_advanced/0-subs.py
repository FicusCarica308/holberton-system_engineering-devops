#!/usr/bin/python3
"""Module contains singular function"""
import requests


def number_of_subscribers(subreddit):
    """Finds the amount of subscribers from a given subreddit"""
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'MannyAgent V1',
        }
    )
    subs = requests.get('https://www.reddit.com/r/{}/about.json'.
                        format(subreddit), headers=headers)
    if subs.reason != 'OK':
        return 0
    else:
        return (subs.json()['data']['subscribers'])
