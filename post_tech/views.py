from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

from post_tech.models import PostTech

@login_required(login_url='/login/')
def show_post_tech(request):
    return render(
        request,
        'post_tech_index.html'
    )

def get_tech_post(request):
    posts = PostTech.objects.all()
    return HttpResponse(serializers.serialize('json', posts),
        content_type='application/json'
    )

@login_required(login_url='/login/')
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
