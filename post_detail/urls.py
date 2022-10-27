from django.urls import path
from post_detail.views import *

app_name = 'post-detail'

urlpatterns = [
    path('user-post-detail/<int:key>', show_post_detail, name='show-post-detail'),
    path('add-post-comment/', add_post_comment, name="add-post-comment"),
    path('post-comment-json/', get_post_comment, name="get-tech-post"),
]
