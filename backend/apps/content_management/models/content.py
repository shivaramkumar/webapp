from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import get_valid_filename
from django.utils.translation import gettext as _

from apps.content_management.models.node import BlogNode, NodeType
from apps.core.models import BaseModel


class BaseContentModel(BaseModel):
    node = models.ForeignKey(BlogNode, on_delete=models.CASCADE)

    @staticmethod
    def upload_location(instance: models.Model, filename: str) -> str:
        now = timezone.now()
        data_sub_str = f"{now.year}/{now.month}/{now.day}"
        return f"uploads/{instance._meta.default_related_name}/{data_sub_str}/{get_valid_filename(filename)}"

    def __str__(self) -> str:
        return f"{self.node}-content"

    class Meta:
        abstract = True


class BaseLanguageBasedContentModel(BaseContentModel):
    """
    Base language model
    """

    language_independent = models.BooleanField(
        default=False,
        help_text=_("Select this option, if you want to disable language dependency instance wise"),
    )
    language_code = models.CharField(choices=settings.LANGUAGES, max_length=25)

    def __str__(self) -> str:
        return f"{self.node}-{self.language_code}-content"

    class Meta:
        abstract = True


class BaseTextContentModel(BaseLanguageBasedContentModel):
    """
    Base text content model
    """

    content = models.TextField(help_text=_("Enter some text here"))

    def __str__(self) -> str:
        return f"{self.node}-{self.language_code}-text"

    class Meta:
        abstract = True


class BaseUrlContentModel(BaseLanguageBasedContentModel):
    """
    Base url content model
    """

    url = models.URLField(help_text=_("Enter a url here"))

    def __str__(self) -> str:
        return f"{self.node}-{self.language_code}-url"

    class Meta:
        abstract = True


class BlogArticle(BaseTextContentModel):
    """
    BlogArticle

    Args:
        BaseTextContentModel (extends):
    """

    node = models.ForeignKey(
        BlogNode,
        on_delete=models.CASCADE,
        limit_choices_to={"node_type": NodeType.ARTICLE},
    )

    class Meta:
        verbose_name = _("Blog Article")
        verbose_name_plural = _("Blog Articles")
        default_related_name = "blog_articles"
