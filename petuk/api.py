from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt import views as jwt
from djoser import views

from restaurant.views import CategoryViewSet, RestaurantViewSet, RestaurantImageViewSet, ReviewViewSet, ItemViewSet
from account.views import UserRegistration
from offer.views import OfferViewSet
from trending.views import TrendingViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, base_name='category')
router.register(r'restaurants', RestaurantViewSet, base_name='restaurant')
router.register(r'restaurants/images', RestaurantImageViewSet, base_name='restaurant-images')
router.register(r'items', ItemViewSet, base_name='menu-item')
router.register(r'offers', OfferViewSet, base_name='offer')
router.register(r'trending', TrendingViewSet, base_name='trending')


class RestAPI(object):
    def __init__(self, name='rest_api'):
        self.name = name

    def get_urls(self):
        urlpatterns = [
            url(r'^', include(router.urls)),
            url(r'^api-token-auth/', jwt.obtain_jwt_token),
            url(r'^api-token-refresh/', jwt.refresh_jwt_token),
            url(r'register', UserRegistration.as_view(), name="register"),
            url(r'^password/$', views.SetPasswordView.as_view(), name='set_password'),
            url(r'^password/reset/$', views.PasswordResetView.as_view(), name='password_reset'),
            url(r'^password/reset/confirm/$', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()


api = RestAPI()

__all__ = ["api", "RestAPI"]
