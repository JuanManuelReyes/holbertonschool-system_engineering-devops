#!/usr/bin/python3
"""asd"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return the sub number
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        headers = requests.utils.default_headers()

        headers.update({'User-Agent': 'My User Agent 1.0'})

        res = requests.get(url, headers=headers, params={'after': after})

        res_json = res.json()

        child = res_json['data']['children']

        for title in child:
            hot_list.append(title['data']['title'])

        after = res_json['data']['after']

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    except Exception:
        return None
