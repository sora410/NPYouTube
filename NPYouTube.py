# coding: utf-8

import appex
import console
import urllib
import requests as r
from my_twitter import MyTwitter

twitter = MyTwitter.account()
url = "https://api.twitter.com/1.1/statuses/update.json"
y_api = 'https://www.googleapis.com/youtube/v3/videos'

def get_youtube_url():
	return appex.get_text()

def get_video_id(youtube_url):
	params = urllib.parse.urlparse(youtube_url)
	query = params.query
	parsed = urllib.parse.parse_qs(query)
	return parsed['v'][0]

def get_snippet(id):
	result = r.get(y_api, params={
		'part': 'snippet', 
		'id': id, 
		'key': '', # YouTube API key
		'maxResults': 1
	}).json()
	return result['items'][0]['snippet']

def get_title(snippet):
	return snippet['title']

def tweet(title, youtube_url):
	txt = '#NowPlaying - %s via YouTube %s' % (title, youtube_url)
	twitter.post(url, {'status': txt})

def main():
	youtube_url = get_youtube_url()
	id          = get_video_id(youtube_url)
	snippet     = get_snippet(id)
	title       = get_title(snippet)
	tweet(title, youtube_url)
	console.hud_alert('tweeted!','success')

main()
