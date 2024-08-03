#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""

from requests import get

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).
        after (str): The pagination parameter to fetch the next set of results (default None).

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        params = {'after': after, 'limit': 100}
        headers = {'User-Agent': 'my-app/0.0.1'}

        req = get(url, params=params, headers=headers, allow_redirects=False)
        
        # Handle invalid subreddit or request failure
        if req.status_code != 200:
            return None
        
        # Extract data from the response
        data = req.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])
        
        # Add article titles to the list
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        # Recursively fetch more data if 'after' is available
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    return None
