from django.conf.urls import url
from line_graph import views

app_name = 'line_graph'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graph/', views.graph, name='graph'),
    url(r'^add/$', views.edit, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]