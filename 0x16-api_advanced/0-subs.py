#!/usr/bin/python3
"""A function define that queries the Reddit API.

Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
"""
from requests import get

def number_of_subscribers(subreddit):
    """This function defines  queries the Reddit API to get the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    if subreddit and isinstance(subreddit, str):
        subs = 0
        url = f'https://reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'my-app/0.0.1'}
        try:
            req = get(url, headers=headers)
            if req.status_code == 200:
                data = req.json()
                subs = data.get('data', {}).get('subscribers', 0)
        except Exception:
            pass
        return subs
    return 0
