from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('log_user_in/', views.LogInView, name='log_user_in'),
]