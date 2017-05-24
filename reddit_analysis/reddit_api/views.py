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
	r = praw.Reddit(client_id='E__vNDwXxkyPjQ',
				client_secret='aShhA_loQQT3l23p0uvjahQBAMg',
				user_agent='insert user agent')
	page = r.subreddit('aww')
	top_posts = page.hot(limit=None)
	for post in top_posts:
		print(post.title, post.ups)
