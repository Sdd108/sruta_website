from django.urls import path
from .views import leave_message_view

app_name = 'home'

urlpatterns = [
    path('leave_message/', leave_message_view, name='leave_message'),
]
