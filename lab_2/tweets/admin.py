from django.contrib import admin
from tweets.models import Tweet

admin.site.register(Tweet)

def __str__(self):
	return self.text
