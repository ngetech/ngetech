from django.urls import path
from discussion_forum.views import *

app_name = 'discussion_forum'

urlpatterns = [
    path('', discussion, name='discussion'),
    path('get-discussion/', get_discussion, name='get-discussion'),
    path('post-discussion-forum/', add_discussion, name='add-discussion'),
]