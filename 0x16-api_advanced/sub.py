#!/usr/bin/python3
import requests

api_url = 'https://www.reddit.com/r/movies/about.json'
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Reddit API script)'}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print('the connection to the api was successful')
    data = response.json()
    subs = data["data"]["subscribers"]
    print(subs)
elif response.status_code ==  404:
    print('unable to reach the url')

else:
    print('unable to reach the api')
