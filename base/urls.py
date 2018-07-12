from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'channels/$', views.ChannelView.as_view(), name='channel-list'),
    re_path(r'channels/(?P<pk>\d+)/$', views.ChannelView.as_view(), name='channel-detail'),
    re_path(r'^channels/(?P<pk>\d+)/messages/$', views.message_list, name='message-list'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register_view, name='register'),
    re_path(r'^logged/$', views.logged_view, name='logged')
]
