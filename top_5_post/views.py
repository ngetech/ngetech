from django.shortcuts import render
from post_tech.models import PostTech
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse

# Create your views here.
def show_top5_post(request):
    return render(request,'top_5.html')
    
def get_top5_post(request):
    posts = PostTech.objects.all().order_by('-likes')[:5]
    return HttpResponse(serializers.serialize('json', posts),content_type='application/json')
