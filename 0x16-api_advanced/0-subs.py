#!/usr/bin/python3
"""A function that queries the Reddit API to get the number of subscribers."""

import requests

def number_of_subscribers(subreddit):
    """This function queries the Reddit API to get the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    headers = {'User-Agent': 'my_user_agent'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0