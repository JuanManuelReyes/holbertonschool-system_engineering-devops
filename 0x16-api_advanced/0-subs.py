#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ 
    Return the sub number
    https://stackoverflow.com/questions/
    10606133/%20sending-user-agent-using-requests-library-in-python

    https://developer.mozilla.org/en-US/docs/Web/HTTP/
    Status#successful_responses
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = requests.utils.default_headers()
    
    headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
    )
    
    res = requests.get(url, headers=headers)
    
    res_json = res.json()
    
    if res.status_code <= 200:
        return res_json['data']['subscribers']
    else:
        return 0