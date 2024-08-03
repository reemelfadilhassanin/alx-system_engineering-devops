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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    data = response.json().get("data", {})
    if not data:
        print("No data found.")
        return None

    children = data.get("children", [])
    after = data.get("after", None)
    
    if not children:
        print("No children found.")
        return hot_list

    for item in children:
        title = item.get("data", {}).get("title", "")
        hot_list.append(title)

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

