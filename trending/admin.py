from django.contrib import admin
from .models import Trending


@admin.register(Trending)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant',]
    list_filter = ('restaurant',)