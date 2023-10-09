from django.urls import path

from apps.content_management.views import DashboardView

urlpatterns = [path("", DashboardView.as_view(), name="dashboard")]
