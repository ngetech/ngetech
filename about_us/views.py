from django.shortcuts import render

def about_us(request):
    return render(
        request,
        'about_us_index.html'
    )
