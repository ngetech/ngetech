from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound,JsonResponse
from post_tech.forms import PostTechForm

from post_tech.models import PostTech

def show_post_tech(request):
    return render(
        request,
        'post_tech_index.html',
        {
            'form': PostTechForm()
        }
    )

@csrf_exempt
def get_tech_post(request):
    posts = PostTech.objects.order_by('?')
    return HttpResponse(serializers.serialize('json', posts),
        content_type='application/json'
    )

@login_required(login_url='/login/')
@csrf_exempt
def add_post_tech(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        if  title is not None and description is not None:
            post = PostTech.objects.create(
                user=user,
                username=user,
                title=title,
                description=description
            )
            return HttpResponse(f"Succesfully create discussion (id: {post.pk})")
    return HttpResponseBadRequest("Bad request")

@login_required(login_url='/login/')
@csrf_exempt
def add_likes(request, key):
    try:
        if request.method == 'POST':
            post = PostTech.objects.get(pk=key)
            is_like = False

            for like in post.likes.all():
                if like == request.user:
                    is_like = True
                    break
            
            if not is_like:
                post.likes.add(request.user)
            
            if is_like:
                post.likes.remove(request.user)

            return JsonResponse({'error': False})
        return HttpResponseBadRequest("Bad request")
    except:
        return HttpResponseNotFound(f"User not exist in likes with post id: {id}")

