# Generated by Django 5.1 on 2024-09-18 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_is_published_product_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductVersion",
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
                ("number", models.PositiveIntegerField(verbose_name="Номер версии")),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название версии"),
                ),
                (
                    "is_active",
                    models.BooleanField(verbose_name="Признак текущей версии"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
