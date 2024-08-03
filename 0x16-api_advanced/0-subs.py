#!/usr/bin/python3
"""A function define that queries the Reddit API.

Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
"""

import requests
def number_of_subscribers(subreddit):
    """This function defines  queries the Reddit API to get the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
	
url_base = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
response = requests.get(url_base, headers=headers, allow_redirects=False)
if response.status_code == 404:
    return 0
results = response.json().get("data")
return results.get("subscribers")
