from django.conf.urls import patterns, url
from indata import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^index/', views.index, name='index'),
        url(r'^choice_section/$', views.choice_section, name='choice_section'),
        url(r'^choice_chapter/$', views.choice_chapter, name='choice_chapter'),
        )
