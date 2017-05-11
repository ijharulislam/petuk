from django.conf.urls import url, include
from rest_framework import routers

from restaurant.views import CategoryViewSet, RestaurantViewSet, RestaurantImageViewSet, ReviewViewSet, MenuViewSet, MenuItemViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, base_name='category')
router.register(r'restaurants', RestaurantViewSet, base_name='restaurant')
router.register(r'restaurants/images', RestaurantImageViewSet, base_name='restaurant-images')
router.register(r'menus', MenuViewSet, base_name='menu')
router.register(r'menu-items', MenuItemViewSet, base_name='menu-item')


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
