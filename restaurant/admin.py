from django.contrib import admin

from .models import *


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 4


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ RestaurantImageInline, ReviewInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ('name', )


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 4


class ItemReviewInline(admin.TabularInline):
    model = ItemReview
    extra = 2


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ('name',)
    inlines = [ItemImageInline, ItemReviewInline]