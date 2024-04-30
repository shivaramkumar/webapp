import django.views.generic as generic_views
from rest_framework import viewsets

from apps.content_management.models.content import BlogArticle
from apps.content_management.models.serializers import BlogArticleSerializer


class DashboardView(generic_views.TemplateView):
    template_name = "content_management/dashboard.html"


class BlogArticleViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
