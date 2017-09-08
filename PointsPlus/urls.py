from django.conf.urls import url

from . import views

app_name="points" # 和html中:前的名称匹配 
urlpatterns=[
    url(r'^$',views.index,name='index'),
    # /points/help
    url(r'^help/$',views.help,name='help'),
    # /points/notice
#     url(r'^notice/$',views.notice,name='notice'),
    url(r'^notice/$',views.NoticeView.as_view(),name='notice'),
#     url(r'^notice/(?P<user_id>[0-9]+)$',views.detail,name='detail'),
    url(r'^notice/(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),
    # /points/edit
    url(r'^edit/(?P<user_id>[0-9]+)$',views.edit,name='edit'),
    url(r'^submit/(?P<user_id>[0-9]+)$',views.submit,name='submit'),
]