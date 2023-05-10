#!/usr/bin/python3

"""
importing requests module ====
"""

from requests import get


def top_ten(subreddit):
    """
    --------------------------------------------------
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 112.0.5615.139'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    all_data = response.json()

    try:
        firstraw = all_data.get('data').get('children')

        for i in firstraw:
            print(i.get('data').get('title'))

    except:
        print("None")
