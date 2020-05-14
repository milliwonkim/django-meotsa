from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import blogpost.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogpost.views.read_blog_list, name="read_blog_list"),
    path('blog/new', blogpost.views.blog_new, name="blog_new"),
    path('blog/create', blogpost.views.create_blog, name="create_blog"),
    path('blog/detail/<int:blog_id>', blogpost.views.read_blog_one, name="read_blog_one"),
    path('blog/update/<int:pk>', blogpost.views.update_blog, name="update_blog"),
    path('blog/delete/<int:pk>', blogpost.views.delete_blog, name="delete_blog"),

    path('signup/', account.views.signup, name="signup"),
    path('login/', account.views.login, name="login"),
    path('logout/', account.views.logout, name="logout"),
]
