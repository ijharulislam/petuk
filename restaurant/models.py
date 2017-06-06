import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True,
                            help_text='Comma-delimited set of SEO keywords for meta tag')

    class Meta:
        db_table = 'categories'
        ordering = ('id',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.name)


class Restaurant(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, default="Dhaka")
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    logo = models.ImageField(upload_to='media/restaurant', blank=True, null=True)
    featured_image = models.ImageField(upload_to='media/restaurant', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    tags = models.CharField(max_length=100, null=True, blank=True,
                            help_text='Comma-delimited set of SEO keywords for meta tag')

    class Meta:
        db_table = 'restaurants'
        ordering = ('id',)
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def ratings(self):
        rating = 0
        reviews = Review.objects.filter(restaurant=self)
        for review in reviews:
            rating += review.rating
        if rating:
            avg = rating / reviews.count()
            return avg
        else:
            return 'No reviews yet!'


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images')
    image = models.ImageField(upload_to='media/restaurant')


class Review(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.restaurant.name)


class Item(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def ratings(self):
        rating = 0
        reviews = ItemReview.objects.filter(item=self)
        for review in reviews:
            rating += review.rating
        if rating:
            avg = rating / reviews.count()
            return avg
        else:
            return 'No reviews yet!'


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images')
    image = models.ImageField(upload_to='media/restaurant/menu')


class ItemReview(models.Model):
    user = models.CharField(max_length=250, blank=True, null=True)
    item = models.ForeignKey('Item')
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.item.name)