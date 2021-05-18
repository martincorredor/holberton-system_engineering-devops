#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """If not a valid subreddit, print None."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    req = requests.get(url, headers=headers).json()
    ten = req.get('data', {}).get('children', [])
    if not ten:
        print(None)
    for i in ten:
        print(i.get('data').get('title'))
