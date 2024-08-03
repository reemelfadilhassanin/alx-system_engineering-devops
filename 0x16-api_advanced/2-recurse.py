#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""
import pprint
import requests

url = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[]):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    headers = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(url.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)