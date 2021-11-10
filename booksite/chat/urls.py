from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    #path('', views.chat, name='chat'),    
    #path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    #path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    #path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
]
