#!/usr/bin/python3
"""A function that queries the Reddit API to print the titles of the top 10 hot posts."""
import requests

def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: If the subreddit is invalid or if the request fails.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Linux:top_ten:v1.0.0 (by /u/your_username)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json().get('data', {})
                posts = data.get('children', [])
                for post in posts[:10]:
                    print(post.get('data', {}).get('title', ''))
            except (KeyError, TypeError) as e:
                print("JSON Parsing Error:", e) 
                print(None)
        else:
            print(None)
    except requests.RequestException as e:
        print("Request Exception:", e)
        print(None)
