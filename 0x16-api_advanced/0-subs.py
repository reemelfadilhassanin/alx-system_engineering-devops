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
    headers = {'User-Agent': 'CustomClient/1.0'}
    try:
        response = requests.get(url_base, headers=headers, allow_redirects=False)
        
        print("Status Code: {}".format(response.status_code))
        print("Headers: {}".format(response.headers))

        if response.status_code == 200:
            response_json = response.json()
            print("Response JSON: {}".format(response_json))
            
            if 'data' in response_json:
                return response_json['data'].get('subscribers', 0)
        else:
            print("Error response received: {}".format(response.status_code))
    
    except requests.RequestException as e:
        print("Request Exception: {}".format(e))

    return 0
