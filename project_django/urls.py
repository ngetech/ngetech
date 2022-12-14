"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('about-us/', include('about_us.urls')),
    path('post-tech/', include('post_tech.urls')),
    path('admin/', admin.site.urls),
    path('discussion/', include('discussion_forum.urls')),
    path('post-detail/', include('post_detail.urls')),
    path('top-5-post/', include('top_5_post.urls')),
    path('tech-survey/', include('tech_survey.urls')),
]
