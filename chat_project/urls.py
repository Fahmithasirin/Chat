from django.urls import path
from call import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', views.chat_home, name='chat_home'),
    path('chat/messages/<int:user_id>/', views.fetch_messages, name='fetch_messages'),
    path('chat/send/', views.send_message, name='send_message'),
]
