from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register(r'jobs', JobApplication, basename='Job')


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls')),


]