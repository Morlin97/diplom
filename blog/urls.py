from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>[0-9]+)/approve/', views.comment_approve, name='comment_approve'),
    url(r'^post/(?P<pk>[0-9]+)/remove/', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>[0-9]+)/give_mark/(?P<_mark>[0-9]+)', views.comment_mark, name='give_mark'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)