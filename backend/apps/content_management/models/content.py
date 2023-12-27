from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from apps.content_management.models.node import BlogNode, NodeType
from apps.core.models import BaseModel


class BaseContentModel(BaseModel):
    node = models.ForeignKey(BlogNode, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.node}-content"

    class Meta:
        abstract = True


class BaseLanguageContentModel(BaseContentModel):
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


class BaseTextContentModel(BaseLanguageContentModel):
    """
    Base text content model
    """

    content = models.TextField(help_text=_("Enter some text here"))

    def __str__(self) -> str:
        return f"{self.node}-{self.language_code}-text"

    class Meta:
        abstract = True


class BaseUrlContentModel(BaseLanguageContentModel):
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
