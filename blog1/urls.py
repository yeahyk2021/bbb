"""blog1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from myblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('blog', views.blog, name="blog"), #主页跳转到博客里面
    path('about/', views.about, name="about"), #主页跳转到博客里面
    path('contact/', views.contact, name="contact"), #主页跳转到联系页面
    path('ueditor/', include('DjangoUeditor.urls')),
    path('retail-<int:id>.html', views.retail, name='retail'),#内容页
   # path('retail/', views.retail,name='retail'),
]
