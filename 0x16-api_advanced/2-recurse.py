#!/usr/bin/python3
"""A function that recursively queries the Reddit API to get all hot articles from a subreddit."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate the titles (default empty).
        after (str): The pagination parameter to fetch the next set of results (default None).

    Returns:
        list: A list of all hot article titles or None if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list