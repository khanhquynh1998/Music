from django.urls import path
from web import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]