from django.db import models
from restaurant.models import Restaurant, Item
from offer.models import Offer


class Trending(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='trending')
    item = models.ForeignKey(Item, related_name='trending_itmes')
    offer = models.ForeignKey(Offer, related_name='trending_offers')
    gist = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'Restaurant:{0}, item:{1}'.format(self.restaurant.name, self.item.name)
