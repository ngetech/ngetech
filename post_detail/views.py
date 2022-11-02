from django.shortcuts import render
from django.shortcuts import redirect
from post_tech.models import PostTech
from post_detail.models import PostComment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from post_detail.forms import PostCommentForm

@login_required(login_url='/login/')
def show_post_detail(request, key):
    post = PostTech.objects.get(pk=key)
    context = {
        'post': post,
        'form': PostCommentForm()
    }
    return render(request, 'post_detail_index.html', context)

@login_required(login_url='/login/')
@csrf_exempt
def get_post_comment(request):
    posts = PostComment.objects.all()
    return HttpResponse(serializers.serialize('json', posts),
        content_type='application/json'
    )

@login_required(login_url='/login/')
@csrf_exempt
def add_post_comment(request):
    if request.method == 'POST':
        user = request.user
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        PostComment.objects.create(
            user=user,
            username=user,
            post=PostTech.objects.get(pk=post_id),
            comment=comment,
        )
        return JsonResponse({
            'error': False, 
            'msg':'Successful'
        })