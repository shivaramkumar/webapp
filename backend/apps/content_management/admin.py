from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from apps.content_management.models.content import BlogArticle
from apps.content_management.models.node import BlogNode


@admin.register(BlogNode)
class BlogeNodeAdmin(TreeAdmin):
    form = movenodeform_factory(BlogNode)


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "language_code",
    )
