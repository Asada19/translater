from django.urls import path
from .views import *

urlpatterns = [
    path('', word_index, name='word_index'),
    path('word_detail/', word_index, name='word_detail')
]