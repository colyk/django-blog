from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from mysite import settings


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)