from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)


class RestAPI(object):
    def __init__(self, name='rest_api'):
        self.name = name

    def get_urls(self):
        urlpatterns = [
            url(r'^', include(router.urls)),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()


api = RestAPI()

__all__ = ["api", "RestAPI"]
