"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from photos import views as photos_views
from photos import api as photos_api
from users import views as users_views
from users import api as users_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', photos_views.HomeView.as_view(), name="photos_home"),
    path('my-photos', login_required(photos_views.UserPhotosView.as_view()), name="user_photos"),
    path('photos/<int:pk>', photos_views.detail, name="photo_detail"),
    path('photos', photos_views.PhotoListView.as_view(), name="photos_list"),
    path('photos/new', photos_views.create, name="create_photo"),
    path('api/1.0/photos', photos_api.PhotoListAPI.as_view(), name="photo_list_api"),
    path('api/1.0/photo/<int:pk>', photos_api.PhotoDetailAPI.as_view(), name="photo_detail_api"),
    path('login', users_views.LoginView.as_view(), name="users_login"),
    path('logout', users_views.LogoutView.as_view(), name="users_logout"),
    path("api/1.0/users", users_api.UserListAPI.as_view(), name="user_list_api"),
    path("api/1.0/user/<int:pk>", users_api.UserDetailAPI.as_view(), name="user_detail_api")
]
