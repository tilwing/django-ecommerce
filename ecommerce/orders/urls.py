from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>([0-9]+|[A-Z]+|\-)+)/$', views.DetailView.as_view(),
        name='detail'),
    url(r'^new/$', views.order_new, name='order_new'),
    url(r'^(?P<pk>([0-9]+|[A-Z]+|\-)+)/remove/$', views.order_remove,
        name='order_remove'),
    url(r'^(?P<pk>([0-9]+|[A-Z]+|\-)+)/edit/$', views.order_edit,
        name='order_edit'),
]
