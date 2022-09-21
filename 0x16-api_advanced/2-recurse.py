#!/usr/bin/python3
"""asd"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Return the sub number
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = requests.utils.default_headers()

    headers.update({'User-Agent': 'My User Agent 1.0'})

    res = requests.get(url, headers=headers)

    res_json = res.json()
