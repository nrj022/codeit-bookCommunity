from django.urls import path
from . import views

""" path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), """

urlpatterns = [
    path('', views.home, name='home'),
    #path('login', views.login, name='login'),
    path('chat', views.chatRoom, name='chatRoom')
]
