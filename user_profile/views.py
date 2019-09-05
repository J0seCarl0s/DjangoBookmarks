from django.shortcuts import render
from django.views.generic import View
from user_profile.models import User
from tweets.models import Tweet

class Profile(View):

	def get(self, request, username):
		params = {}
		user = User.objects.get(username=username)
		tweets = Tweet.objects.filter(user=user)

		params['tweets'] = tweets
		params['user'] = user

		return render(request, 'profile.html', params)
