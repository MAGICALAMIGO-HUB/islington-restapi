from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import ArticalViewSet
from . import views
router = DefaultRouter()
router.register('api', views.ArticalViewSet)

urlpatterns = [
    # path('home', views.api_home),
    path('', include(router.urls)),
]