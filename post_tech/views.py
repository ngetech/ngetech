from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from post_tech.models import PostTech

# @login_required(login_url='/login/')
def show_post_tech(request):
    return render(
        request,
        'post_tech_index.html'
    )

@login_required(login_url='/login/')
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
        PostTech.objects.create(
            user=user,
            username=user,
            title=title,
            description=description
        )
        return redirect('post-tech:show-post-tech')

    return render(
        request,
        'create_post_tech.html',
        {}
    )

@login_required(login_url='/login/')
@csrf_exempt
def add_likes(request, key):
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

