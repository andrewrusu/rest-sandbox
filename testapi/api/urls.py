from django.conf.urls import include, re_path

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('person', views.PersonViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
]
