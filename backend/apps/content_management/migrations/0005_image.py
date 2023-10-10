# Generated by Django 4.2.6 on 2023-10-08 16:16

import apps.content_management.models.content
import dirtyfields.dirtyfields
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content_management", "0004_blogarticle_language_independent"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name="Created at",
                    ),
                ),
                (
                    "lastmodified_at",
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name="Last modified at",
                    ),
                ),
                ("caption", models.CharField(max_length=255, unique=True)),
                (
                    "file",
                    models.FileField(
                        upload_to=apps.content_management.models.content.BaseContentModel.upload_location,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ("png", "jpg", "svg")
                            )
                        ],
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        default=None,
                        editable=False,
                        null=True,
                        populate_from="caption",
                        unique=True,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "lastmodified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_lastmodified",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last modified by",
                    ),
                ),
                (
                    "node",
                    models.ForeignKey(
                        limit_choices_to={"node_type": 3},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content_management.blognode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
                "default_related_name": "images",
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]