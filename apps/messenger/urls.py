from django.urls import path
from . import views

app_name = 'messenger'
urlpatterns = [
    path('send-message/', views.send_message, name='send_message'),
    path('conversations/', views.show_conversations, name='conversations'),
    path('conversation/<int:conversation_id>', views.show_conversation, name='show_conversation'),
]