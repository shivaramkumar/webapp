from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.core.models import BaseModel


class BaseLanguageBasedContentModel(BaseModel):
    """
    Base language model
    """

    language_code = models.CharField(choices=settings.LANGUAGES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def get_linked_object(self):
        if self.content_object:
            return self.content_object
        else:
            return None

    def __str__(self) -> str:
        return f"{self.content_object}-{self.language_code}-content"

    class Meta:
        abstract = True


class BaseTextContentModel(BaseLanguageBasedContentModel):
    """
    Base text content model
    """

    content = models.TextField(help_text="Enter some text here")

    def __str__(self) -> str:
        return f"{self.content_object}-{self.language_code}-text"

    class Meta:
        abstract = True


class BaseUrlContentModel(BaseLanguageBasedContentModel):
    """
    Base url content model
    """
    url = models.URLField(help_text="enter the url")

    def __str__(self) -> str:
        return f"{self.content_object}-{self.language_code}-url"

    class Meta:
        abstract = True
