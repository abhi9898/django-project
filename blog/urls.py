from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^$', views.SaveProfile, name='post_list'),
    url(r'^profile',views.showProfile,name = 'profile'),
    url(r'^addNotes/',views.addNotes,name = 'addNotes'),
    url(r'^mail/$',views.Email,name = 'Email'),
]