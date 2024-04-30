from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.content_management.views import DashboardView

from .views import BlogArticleViewSet

router = DefaultRouter()
router.register(r'blogarticle', BlogArticleViewSet)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path('', include(router.urls)),
]
