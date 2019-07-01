from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="main"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.sign_in, name="sign-in"),
    path('new_topic/', views.new_topic, name="new-topic"),
    path('topic/<topic_id>', views.topic_detail, name="topic-detail"),
    path('add_post/', views.add_post, name="add-post"),
    path('delete_post/', views.delete_post, name="delete-post"),
    path('signup/', views.signup, name="sign-up"),
]
