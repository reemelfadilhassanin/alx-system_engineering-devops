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

url = f'https://www.reddit.com/r/{subreddit}/about.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
try:
        
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
        	return 0
except Exception:
    return 0