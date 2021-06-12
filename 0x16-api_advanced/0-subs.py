#!/usr/bin/python3
"""
Working with Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = {'User-Agent': 'termi'}
    try:
        req = requests.get(url, headers=agent, allow_redirects=False).json()
        a = req.get('data').get('subscribers')
    except:
        return 0
    return a
