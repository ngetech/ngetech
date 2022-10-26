from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def show_post_tech(request):
    return render(
        request,
        'post_tech_index.html'
    )

@login_required(login_url='/login/')
def add_post_tech(request):
    if request.method == 'POST':
        pass
    
    return render(
        request,
        'create_post_tech.html'
    )

