from django.urls import path
from top_5_post.views import *

app_name = 'top_5_post'

urlpatterns = [
    path('', show_top5_post, name='show_top5_post'),
    path('top-post-json/', get_top5_post, name='top-post-json'),
]
