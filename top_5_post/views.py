from django.shortcuts import render
from post_tech.models import PostTech
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def show_top5_post(request):
    return render(request,'top_5.html')
    
def get_top5_post(request):
    posts = list(PostTech.objects.all())
    return HttpResponse(serializers.serialize('json', posts),content_type='application/json')
