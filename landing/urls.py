from django.conf.urls import url
from landing.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
