import django.views.generic as generic_views


class DashboardView(generic_views.TemplateView):
    template_name = "content_management/dashboard.html"
