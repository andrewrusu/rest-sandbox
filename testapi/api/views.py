from rest_framework import mixins, viewsets

from . import models
from . import serializers


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = serializers.PersonSerializer

    queryset = models.Person.objects.all()

    http_method_names = ['get', 'post', 'put', 'patch' 'delete']
