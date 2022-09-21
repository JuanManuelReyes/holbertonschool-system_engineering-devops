#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ Return the sub number"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = requests.utils.default_headers()
    
    headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
    )
    
    res = requests.get(url, headers=headers).json()
    
    subs = res['data']['subscribers']
    
    return subs