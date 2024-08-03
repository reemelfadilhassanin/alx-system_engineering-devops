#!/usr/bin/python3
"""A function that queries the Reddit API

	Returns:
		the number of subscribers
	"""
import requests
url = 'http://reddit.com/r/{}/about.json'

def number_of_subscribers(subreddit):
	"""This to define queries the Reddit API

	Args:
		subreddit (str): The name of the subreddit to query.

	Returns:
		int: The number of subscribers if is valid, otherwise 0.
	"""

headers = {'User-agent': 'Unix:0-subs:v1'}
response = requests.get(url.format(subreddit),
							headers=headers)
if response.status_code != 200:
	return 0
return response.json().get('data', {}).get('subscribers', 0)