from django.contrib import admin
from discussion_forum.models import ForumDiscussion, ForumReply

# Register your models here.
admin.site.register(ForumDiscussion)
admin.site.register(ForumReply)