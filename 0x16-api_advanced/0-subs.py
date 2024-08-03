#!/usr/bin/python3
"""A function that queries the Reddit API

	Returns:
		the number of subscribers
	"""
from requests import get



def number_of_subscribers(subreddit):
	"""This to define queries the Reddit API

	Args:
		subreddit (str): The name of the subreddit to query.

	Returns:
		int: The number of subscribers if is valid, otherwise 0.
	"""

	if subreddit and type(subreddit) is str:
			subs = 0
			url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
			headers = {'user-agent': 'my-app/0.0.1'}
			req = get(url, headers=headers)
			if req.status_code == 200:
				data = req.json()
				subs = data.get('data', {}).get('subscribers', 0)
			return subs