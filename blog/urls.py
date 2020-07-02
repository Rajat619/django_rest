from django.urls import path, include
# from app import views
from rest_framework.routers import DefaultRouter
from blog.views import BlogView

router = DefaultRouter()
router.register(r'api/blogs', BlogView, basename='blog')
urlpatterns = router.urls
