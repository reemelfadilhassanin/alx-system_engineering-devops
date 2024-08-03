#!/usr/bin/python3
"""A function that queries the Reddit API.

Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
"""

import requests

def number_of_subscribers(subreddit):
    """This function queries the Reddit API to get the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url_base = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Linux:0x16-api_advanced:v1.0.0'}
    response = requests.get(url_base, headers=headers, allow_redirects=False)
    if response.status_code == 404:
            return 0
            response_json = response.json().get("data")
            return response_json.get('subscribers')
  
