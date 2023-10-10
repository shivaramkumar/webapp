from django.db import models
from django.utils.translation import gettext as _
from treebeard.mp_tree import MP_Node

from apps.core.models import BaseModel


class NodeType(models.IntegerChoices):
    """
    Args:
        models (_type_): _description_
    """

    SECTION = 1, "SECTION"
    SUBSECTION = 2, "SUBSECTION"
    ARTICLE = 3, "ARTICLE"


class BlogNode(BaseModel, MP_Node):
    name = models.CharField(
        max_length=40, help_text=_("enter a name for the node element")
    )
    node_type = models.IntegerField(
        choices=NodeType.choices, help_text=_("enter the type of node")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Blog Node")
        verbose_name_plural = _("Blog Nodes")
        default_related_name = "blog_nodes"
