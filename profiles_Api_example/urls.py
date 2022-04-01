from django.urls import path, include
from profiles_Api_example import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('hello-viewset', views.helloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello/', views.helloApiView.as_view()),
    path('', include(router.urls))
]

