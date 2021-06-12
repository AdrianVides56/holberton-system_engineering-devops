#!/usr/bin/python3
"""
Working with Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    agent = {'User-Agent': 'termi'}
    try:
        req = requests.get(url, headers=agent, allow_redirects=False).json()
        hot_list.append(req.get('data').get('children'))
        if req.get('data').get('after'):
            return recurse(subreddit, hot_list=hot_list,
                           after=req.get('data').get('after'))
        else:
            return hot_list
    except:
        return None
