from django.urls import path
from .views import index, top_sellers, advertisement_post

urlpatterns=[
    path('',index, name='index'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
]