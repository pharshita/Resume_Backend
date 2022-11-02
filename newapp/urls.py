from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register(r"listjob", JobList, basename="Joblist")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("contect/", ContectForm.as_view(), name="contactform"),
    path("jobs/", JobApplications.as_view(), name="jobs"),
]
