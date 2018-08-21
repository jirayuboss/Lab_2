from django.conf.urls import url
from django.contrib import admin
from tweets.views import Index, Profile

admin.autodiscover()

urlpatterns = [
	url(r'^$', Index.as_view()),
	url(r'^user/(\w+)/$', Profile.as_view()),
	url(r'^admin/', admin.site.urls),
]
