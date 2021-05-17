#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    req = requests.get(url, headers=headers).json()
    subscribers = req.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
