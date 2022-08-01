"""Resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django import views
# from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from newapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from newapp import views
from django.conf import settings
from django.conf.urls.static import static
# from newapp.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/',TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/login/refresh/',TokenRefreshView.as_view(),name ='token_refresh'),
    path('api/registers/',RegisterUserView.as_view(),name ='token_obtain_pair'),
    path('api/updateuser/',UserDetailView.as_view()),
    path('api/changepassword/',ChangePasswordView.as_view()),
    # path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/user/',UserListView.as_view()),
    path('api/education/',EducationListView.as_view()),
    path('api/experience/',ExperienceListView.as_view()),
    path('api/skills/',SkillListView.as_view()),
    path('api/alldata/',ResumeListView.as_view()),
    path('api/resume/<int:id>/',ResumedetailView.as_view()),
    # path('api/edit/<int:id>/',EditResumeView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
