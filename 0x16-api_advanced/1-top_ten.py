#!/usr/bin/python3
"""Module contains singular function"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'MannyAgent V2',
        }
    )
    subs = requests.get('https://www.reddit.com/r/{}/hot.json'.
                        format(subreddit), headers=headers,
                        params={'limit': 10})
    if subs.reason != 'OK':
        print('None')
    else:
        topics = subs.json()['data']['children']
        for item in topics:
            print(item['data']['title'])
