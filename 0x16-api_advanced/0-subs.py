#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Reddit API script)'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subs = data["data"]["subscribers"]
        return subs
    elif response.status_code == 404:
        return 0
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
