#!/usr/bin/python3
"""A recursive function to query Reddit API and count occurrences of keywords in hot articles."""

import requests
import re

def count_words(subreddit, word_list):
    """Recursively fetch all hot articles' titles from a subreddit and count keyword occurrences.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the article titles.

    Returns:
        None
    """
    def recurse(subreddit, hot_list=None, after=None):
        """Helper recursive function to fetch hot articles."""
        if hot_list is None:
            hot_list = []
        
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"}
        params = {"after": after, "limit": 100}
        
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 404:
            return None
        elif response.status_code != 200:
            return None
        
        results = response.json().get("data", {})
        after = results.get("after")
        
        for child in results.get("children", []):
            title = child.get("data", {}).get("title", "").lower()
            hot_list.append(title)
        
        if after:
            return recurse(subreddit, hot_list, after)
        
        return hot_list

    def count_keywords(titles, words):
        """Helper function to count keyword occurrences."""
        keyword_count = {word: 0 for word in words}
        for title in titles:
            for word in words:
                keyword_count[word] += len(re.findall(r'\b{}\b'.format(re.escape(word.lower())), title))
        return keyword_count

    hot_list = recurse(subreddit)
    
    if hot_list is None:
        return
    
    word_counts = count_keywords(hot_list, word_list)
    
    sorted_word_counts = sorted(
        ((word, count) for word, count in word_counts.items() if count > 0),
        key=lambda x: (-x[1], x[0])
    )
    
    for word, count in sorted_word_counts:
        print("{}: {}".format(word, count))

