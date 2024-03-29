#!/usr/bin/python3
"""
====================================
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    -------------------------------------------
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 112.0.5615.139'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')

    except:
        return 0
