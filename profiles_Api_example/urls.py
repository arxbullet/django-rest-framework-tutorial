from django.urls import path, include
from profiles_Api_example import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

#viewsets registro
router.register('hello-viewset', views.helloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

#apiviews registro
urlpatterns = [
    path('hello/', views.helloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]

