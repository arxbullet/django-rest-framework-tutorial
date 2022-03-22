from django.urls import path
from profiles_Api_example import views

urlpatterns = [
    path('hello/', views.helloApiView.as_view()),
]