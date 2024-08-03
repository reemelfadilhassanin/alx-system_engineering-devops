#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""

import requests

url = 'https://www.reddit.com/r/{}/hot.json'

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).
        after (str): The pagination parameter to fetch the next set of results.

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    headers = {'User-Agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    response = requests.get(url.format(subreddit), headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    after = data.get('after')
    
    if not after:
        after = "STOP"
    
    hot_list.extend(post.get('data', {}).get('title') for post in data.get('children', []))
    
    if after == "STOP":
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
