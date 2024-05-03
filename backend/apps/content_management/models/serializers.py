from rest_framework import serializers

from apps.content_management.models.content import BlogArticle


class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = '__all__'
