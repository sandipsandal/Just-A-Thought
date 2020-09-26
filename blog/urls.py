from django.contrib import admin
from django.urls import path, include 
from . import views
from blog import views
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # API to post a comment
    path('postComment', views.postComment, name="postComment"), # we put this path at starting bcoz when comment on post it find his path comment
    path('blog/userPost', views.userPost, name='userPost'),
    path('userPost', views.userPost, name='userPost'),
    
    path('<str:slug>', views.blogPost, name='blogPost'),
    path('', views.blogHome, name='blogHome'),
    # path('blog/userPost', views.categoryName,name="category"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)