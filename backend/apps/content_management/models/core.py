from datetime import timezone

from django.db import models
from django.utils.text import get_valid_filename


def upload_location(instance: models.Model, filename: str) -> str:
    now = timezone.now()
    data_sub_str = f"{now.year}/{now.month}/{now.day}"
    return f"uploads/{instance._meta.default_related_name}/{data_sub_str}/{get_valid_filename(filename)}"
