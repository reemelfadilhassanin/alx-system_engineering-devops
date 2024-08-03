#!/usr/bin/python3
"""A function that queries the Reddit API to print the titles of the top 10 posts"""

import requests

def top_ten(subreddit):
    """print the titles of the first 10 hot posts of subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: If the subreddit is invalid or if the request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Linux:top_ten:v1.0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                print(post['data']['title'])
        except KeyError:
            print(None)
    else:
        print(None)
