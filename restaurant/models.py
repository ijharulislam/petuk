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
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, default="Dhaka")
    postal_code = models.CharField(max_length=250, blank=True, null=True)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    delivery = models.NullBooleanField()
    buffet = models.NullBooleanField()
    outdoor_seating = models.NullBooleanField()
    party_room = models.NullBooleanField()
    accepts_reservations = models.NullBooleanField()
    has_carryouts = models.NullBooleanField()
    has_kids_menu = models.NullBooleanField()
    has_wifi = models.NullBooleanField()
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
        return '{}'.format(self.name)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    available = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return '{}'.format(self.name)
