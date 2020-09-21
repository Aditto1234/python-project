from django.urls import path
from .views import *

urlpatterns = [
    path('',base),
    path('new',new),
    path('category/<int:cid>/',category),

]
