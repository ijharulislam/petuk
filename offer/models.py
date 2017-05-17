from django.db import models

from restaurant.models import Restaurant, Item


class Offer(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='offers')
    item = models.ForeignKey(Item, related_name='item_offers')
    validity = models.DateField()
    gist = models.TextField()
    price = models.FloatField(default=0.0)
    discount = models.IntegerField(default=0)
    offer_amount = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Restaurant:{0}, offer:{1}'.format(self.restaurant.name, self.offer_amount)

    @property
    def offer_amount(self):
        return self.price * (100/self.discount)
