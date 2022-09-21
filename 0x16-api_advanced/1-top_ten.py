#!/usr/bin/python3
"""asd"""

import requests


def top_ten(subreddit):
    """
    Return the sub number
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = requests.utils.default_headers()

    headers.update(
    {'User-Agent': 'My User Agent 1.0'})

    res = requests.get(url, headers=headers)

    res_json = res.json()

    if res.status_code <= 200:
        counter = 0
        while (counter < 10):
            print (res_json['data']['children'][counter]['data']['title'])
            counter += 1
    else:
        print("None")
