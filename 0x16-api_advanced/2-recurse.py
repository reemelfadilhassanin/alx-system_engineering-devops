#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None, count=0):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).
        after (str): The pagination parameter to fetch the next set of results (default None).
        count (int): The number of articles fetched so far (default 0).

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    if hot_list is None:
        hot_list = []
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += len(results.get("children", []))
    
    for child in results.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    
    if after:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list
