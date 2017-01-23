import requests
import re
from bs4 import BeautifulSoup


TWITTER_REQUEST_TEMPLATE = 'https://twitter.com/aaa/status/'

def get_tweet_by_id(in_id):
    response_content = requests.get(TWITTER_REQUEST_TEMPLATE + str(in_id), allow_redirects=True).content
    soup = BeautifulSoup(response_content, 'html.parser')
    title = soup.find('title')
    tweet_text = re.findall('Twitter: "@\w+ (.+)"</title>$', str(title))
    return tweet_text[0] if len(tweet_text) else None
 
