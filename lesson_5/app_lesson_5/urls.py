from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_detail

urlpatterns=[
    path('',index, name='index'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv_detail')
]