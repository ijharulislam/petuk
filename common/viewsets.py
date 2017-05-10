import time

from rest_framework.viewsets import ModelViewSet

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters


class WebAPIView(generics.GenericAPIView):
    def dispatch(self, request, *args, **kwargs):
        global dispatch_time
        global render_time

        dispatch_start = time.time()
        ret = super(WebAPIView, self).dispatch(request, *args, **kwargs)

        render_start = time.time()
        ret.render()
        render_time = time.time() - render_start

        dispatch_time = time.time() - dispatch_start

        return ret


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           viewsets.ViewSetMixin, WebAPIView):
    """
    A viewset that provides default 'list()' and 'retrieve()' actions.
    """
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )


class BaseModelViewSet(ModelViewSet, WebAPIView):

    """
    A viewset that provides default 'create()', 'retrieve()', 'update()',
    'partial_update()', 'destroy()' and 'list()' actions.
    """
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = '__all__'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(BaseModelViewSet, self).update(request, *args, **kwargs)
