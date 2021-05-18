#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """If not a valid subreddit, return None."""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'xio'})
    if requests.get(url, headers=headers, allow_redirects=False):
        if after is None:
            return hot_list
        json = requests.get(url, headers=headers, allow_redirects=False).json()
        for child in json['data']['children']:
            hot_list.append(child)
        after = json['data']['after']
        return recurse(subreddit, hot_list, after)
    else:
        return None
