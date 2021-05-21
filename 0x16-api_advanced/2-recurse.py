#!/usr/bin/python3
""" Contains python method 'recurse' """
import requests


def recurse(subreddit,  prev_title="NULL", hot_list=[]):
    """
    Description:
        Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If nothing found
    or nonexistent subreddit
    returns None...
    """
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'MannyAgent V3',
        }
    )
    subs = requests.get('https://www.reddit.com/r/{}/hot.json'.
                        format(subreddit), headers=headers,
                        params={'after': prev_title})
    if subs.reason != 'OK':
        return None
    else:
        try:
            topics = subs.json()['data']['children'][0]['data']
        except:
            return hot_list
        prev_title = topics['name']
        hot_list.append(topics['title'])
        print(topics['title'])
        if prev_title not in [None, 'None', 'NULL']:
            return recurse(subreddit, prev_title, hot_list)
        return hot_list
