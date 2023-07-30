from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('create/', views.action_fetch_create_order, name="action_fetch_create_order"),
]