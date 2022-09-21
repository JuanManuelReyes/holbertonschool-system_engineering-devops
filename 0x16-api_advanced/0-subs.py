#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ 
    Return the sub number
    https://stackoverflow.com/questions/
    10606133/%20sending-user-agent-using-requests-library-in-python
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = requests.utils.default_headers()
    
    headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
    )
    
    res = requests.get(url, headers=headers).json()
    
    subs = res['data']['subscribers']
    if not subs:
        return 0
    else:
        return subs