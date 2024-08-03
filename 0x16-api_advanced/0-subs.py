#!/usr/bin/python3
"""A function that queries the Reddit API

	Returns:
		the number of subscribers
	"""
import requests



def number_of_subscribers(subreddit):
	"""This to define queries the Reddit API

	Args:
		subreddit (str): The name of the subreddit to query.

	Returns:
		int: The number of subscribers if is valid, otherwise 0.
	"""

url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
response = requests.get(url, headers=headers, allow_redirects=False)

if response.status_code == 404:
	return 0

results = response.json().get("data")
return results.get("subscribers")