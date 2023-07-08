from django.urls import path, re_path
from . import views



urlpatterns = [
    #re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

]