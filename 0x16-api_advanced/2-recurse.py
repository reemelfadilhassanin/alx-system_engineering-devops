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
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return (None)
    response = response.json()
    if "data" in response:
        data = response.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)