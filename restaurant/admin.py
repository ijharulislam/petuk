from django.contrib import admin

from .models import *


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 5


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ RestaurantImageInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ('name', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ('name',)