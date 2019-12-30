# DEFINES URL PATTERNS FOR LEARNING_LOGS

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # HOME PAGE
    path('', views.index, name='index'),
    # PATH THAT SHOWS ALL TOPICS
    path('topics/', views.topics, name='topics'),
    # DETAIL PAGE FOR A SINGLE TOPIC.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # PAGE FOR ADDING A NEW TOPIC
    path('new_topic/',views.new_topic, name='new_topic'),
    # Path for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Path for editing an entry
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
]
