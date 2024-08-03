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
    url_base = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'myapp:myapp:v1.0 (by /u/yourusername)'
    }
    response = requests.get(url_base, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            response_json = response.json()
            data = response_json.get('data', {})
            subscribers = data.get('subscribers', 0)
            return subscribers
        except (ValueError, TypeError) as e:
            print("Error parsing JSON response: {}".format(e))
    elif response.status_code == 404:
        return 0
    else:
        print("Received unexpected status code {}".format(response.status_code))

    return 0
