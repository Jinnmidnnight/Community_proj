from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('new/', new, name="new"),
    path('detail/<str:community_id>/', detail, name="detail"),
    path('comment/<str:community_id>/', comment, name="comment"),
]