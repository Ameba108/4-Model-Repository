from django.urls import path
from .views import ind, top_sellers, advertisement_post, register, login, profile

urlpatterns=[
    path('',ind, name='index'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile')
]