from django.urls import path
from .views import home, profile, RegisterView, dashboard

urlpatterns = [
    path('', home, name='users-home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]