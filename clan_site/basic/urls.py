from django.conf.urls import url
from . import views

app_name='basic'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    
    url(r'^users/$', views.UsersView.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='user_detail'),

    url(r'^rules/$', views.RulesView.as_view(), name='rules'),
    url(r'^rules/(?P<pk>[0-9]+)/$', views.RulesDetailView.as_view(), name='rule_detail'),
    url(r'^rules/add_rule$', views.add_rule, name='add_rule'),

    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login_handle/$', views.login_handle,name='login_handle'),
    url(r'^logout$', views.logout_view, name='logout'),
]