# Generated by Django 4.2.6 on 2023-10-08 10:35

import django.db.models.deletion
from django.db import migrations, models

import apps.content_management.models.node


class Migration(migrations.Migration):
    dependencies = [
        ("content_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticle",
            name="node",
            field=models.ForeignKey(
                limit_choices_to={
                    "node_type": apps.content_management.models.node.NodeType["ARTICLE"]
                },
                on_delete=django.db.models.deletion.CASCADE,
                to="content_management.blognode",
            ),
        ),
    ]
