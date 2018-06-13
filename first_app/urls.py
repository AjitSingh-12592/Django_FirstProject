from django.conf.urls import url
from first_app import views


urlpatterns = [
    url(r'^$', views.index5, name='index'),
    url(r'^help3/', views.index3, name='index'),
    url(r'^help4/', views.index4, name='index'),
    url(r'^help5/', views.index5, name='index'),
    ]
