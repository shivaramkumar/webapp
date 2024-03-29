from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField
from safedelete import HARD_DELETE

from apps.content_management.constants import ALLOWED_IMAGE_FILE_FORMATS
from apps.content_management.models.content import BaseLanguageContentModel, NodeType
from apps.content_management.models.core import upload_location
from apps.content_management.models.node import BlogNode


class Image(BaseLanguageContentModel):
    """
    Args:
        BaseContentModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    _safedelete_policy = HARD_DELETE
    node = models.ForeignKey(
        BlogNode,
        on_delete=models.CASCADE,
        limit_choices_to={"node_type": NodeType.ARTICLE},
    )
    caption = models.CharField(max_length=255, unique=True)
    file = models.FileField(
        upload_to=upload_location,
        validators=[FileExtensionValidator(ALLOWED_IMAGE_FILE_FORMATS)],
    )
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from="caption")

    def __str__(self) -> str:
        if self.node:
            return f"{self.caption} - {self.node}"
        return self.caption

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        default_related_name = "images"
