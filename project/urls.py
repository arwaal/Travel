"""Travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$','maim.views.home'),
    url(r'^home/$','maim.views.home'),
    url(r'^all_images/$','maim.views.all_images'),
    url(r'^user_create/$','maim.views.user_create'),
    url(r'^image_upload/$','maim.views.image_upload'),
    url(r'^user_search/$','maim.views.user_search'),
    url(r'^login/$','maim.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^update/$','maim.views.update'),
    # url(r'^logout/$','maim.views.logout'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
