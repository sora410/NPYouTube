# coding: utf-8

from requests_oauthlib import OAuth1Session

class MyTwitter:
	'provide twitter api'
	@staticmethod
	def account():
		CONSUMER_KEY = ''
		CONSUMER_SECRET = ''
		ACCESS_TOKEN = ''
		ACCESS_TOKEN_SECRET = ''
		return OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
