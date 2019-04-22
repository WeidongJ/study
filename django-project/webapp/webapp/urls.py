"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp_pruemat import views as pruemat_views

urlpatterns = [
    path('', pruemat_views.index, name='index'),
    path('add/', pruemat_views.add, name='add'), # name 指定对应的html文件20190417
    path('add/<int:a>/<int:b>/', pruemat_views.old_add2_redirect),
    path('new_add/<int:a>/<int:b>/', pruemat_views.add2,name='add2'),
    path('admin/', admin.site.urls),
]
