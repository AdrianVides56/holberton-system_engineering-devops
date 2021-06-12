#!/usr/bin/python3
"""
Working with Reddit API
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    agent = {'User-Agent': 'termi'}
    try:
        req = requests.get(url, headers=agent, allow_redirects=False).json()
        posts = req.get('data').get('children')
        for post in posts:
            print('{}'.format(post.get('data').get('title')))
    except:
        print("None")
