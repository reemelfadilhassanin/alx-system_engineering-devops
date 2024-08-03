#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""

import requests

def recurse(subreddit, hot_list=[]):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Linux:recurse:v1.0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            after = data['data'].get('after')
            
            # Add titles of current page to hot_list
            hot_list.extend(post['data']['title'] for post in posts)
            
            # If there's more data, recursively fetch next page
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
            
        except (KeyError, TypeError):
            return None
    else:
        return None
