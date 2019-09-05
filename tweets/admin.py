from django.contrib import admin
from tweets.models import Tweet

admin.site.register(Tweet)
# Register your models here.

def __unicode__(self):
	return self.text