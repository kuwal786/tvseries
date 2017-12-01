from django.conf.urls import include, url

from . import views

app_name = 'westros'

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^home', views.westros,name='index'),
    url(r'^genres', views.genres),
    url(r'^action-genre', views.action),
    url(r'^comedy-genre', views.comedy),
    url(r'^thanks', views.thanks),
    url(r'^term-&-conditions', views.tc,name='terms'),
    url(r'^password change', views.passwordchange),
    url(r'^login_user', views.login_user,name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$',views.register,name='register'),
]
