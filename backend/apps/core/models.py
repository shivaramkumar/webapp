from ambient_toolbox.models import CommonInfo
from dirtyfields import DirtyFieldsMixin
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class BaseModel(SafeDeleteModel, DirtyFieldsMixin, CommonInfo):
    _safedelete_policy = SOFT_DELETE
