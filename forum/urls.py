from django.conf.urls import url

from . import views

app_name = 'forums'

urlpatterns = [
    #HomePage
    url(r'^$', views.index, name='index'),

    #Show All Topics
    url(r'^topics/$', views.topics, name='topics'),

    #Single Topic Detail Page
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #New Topic Page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #New Entry Page
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Edit Entry Page
    url(r'^edit_entry/(?P<entry_id>\d+)/S', views.edit_entry, name='edit_entry'),
]