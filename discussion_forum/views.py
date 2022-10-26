from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from discussion_forum.models import ForumPost
from discussion_forum.forms import ForumForm
from django.contrib.auth.models import User

# Create your views here.
def discussion(req):
    context = {
        'form': ForumForm()
    }
    return render(req, 'discussion.html', context)

def add_discussion(req):
    if req.method == "POST":
        form = ForumForm(req.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            obj = ForumPost.objects.create(content=content, user=req.user)
            return HttpResponse(serializers.serialize("json", [obj], use_natural_foreign_keys=True), content_type="application/json")
    
    return HttpResponseBadRequest()

def get_discussion(req):
    posts = ForumPost.objects.all()
    return HttpResponse(serializers.serialize("json", posts, use_natural_foreign_keys=True), content_type="application/json")