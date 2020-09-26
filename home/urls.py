from django.contrib import admin
from django.urls import path, include 
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name ='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    # path('addPost', views.addPost, name='addPost'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)