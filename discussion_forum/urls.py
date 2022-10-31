from django.urls import path
from discussion_forum.views import *

app_name = 'discussion_forum'

urlpatterns = [
    path('', discussion, name='discussion'),
    path('create-discussion/', create_discussion, name='create-discussion'),
    path('create-discussion/post/', post_discussion, name='post-discussion'),
    path('get/', get_discussions, name='get-discussions'),
    path('<int:id>/', get_discussion_by_id, name='get-discussion-by-id'),
    path('<int:id>/replies/', get_discussion_replies, name='get-discussion-replies'),
    path('<int:id>/replies/add/', add_discussion_reply, name='add-discussion-reply'),
    path('replies/<int:id>/add/', add_nested_reply, name='add-nested-reply'),
    path('replies/<int:id>/', get_nested_replies, name='get-nested-replies'),
]