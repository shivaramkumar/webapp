from enum import Enum

from django.db import models
from django.utils.translation import gettext as _
from treebeard.models import Node

from apps.core.models import BaseModel


class NodeType(Enum):
    SECTION = 1
    SUBSECTION = 2
    ARTICLE = 3


class BlogNode(BaseModel, Node):
    name = models.CharField(max_length=40, help_text=_("enter a name for the node element"))
    node_type = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in NodeType], help_text=_("enter the type of node")
    )

    class Meta:
        verbose_name = _("Blog Node")
        verbose_name_plural = _("Blog Nodes")
        default_related_name = "blog_nodes"
