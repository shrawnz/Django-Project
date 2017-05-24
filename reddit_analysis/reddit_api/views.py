# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import praw

def index(request):
	reddit()
	return HttpResponse("Hello, world. You're at the polls index.")


def reddit():
	reddit = praw.Reddit(client_id='saksham15082',
					 client_secret='aShhA_loQQT3l23p0uvjahQBAMg',
					 user_agent='hello man')
	# print(reddit.user.me())
	for submission in reddit.subreddit('learnpython').hot(limit=10):
		print(submission.title)