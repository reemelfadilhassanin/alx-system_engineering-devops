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
	

sub = requests.get("https://www.reddit.com/r/{}/about.json"
                   .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
if sub.status_code >= 300:
    return 0

return sub.json().get("data").get("subscribers")