"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from forum.views import forums_view,forum_detail_view,delete_comment
from forum.views import home_view
from accounts.views import login_view,registration_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_view,name="home"),
    path("login/",login_view,name="login"),
    path("reg/",registration_view,name="reg"),
    path("logout/",logout_view,name="logout"),
    path("forums/",forums_view,name="forums"),

    path("forum-detail/<int:forum_id>/",forum_detail_view,name="forum"),
    path("forum-detail/<int:forum_id>/<int:comment_id>/delete",delete_comment,name="delete_comment"),

]
