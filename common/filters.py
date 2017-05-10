import django_filters
from django.db import models


class BaseFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }