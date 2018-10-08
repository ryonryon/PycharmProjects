from django.conf.urls import url
from display_rate import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.get_rate, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]
