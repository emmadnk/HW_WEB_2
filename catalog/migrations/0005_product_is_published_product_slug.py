# Generated by Django 5.1 on 2024-09-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_product_views_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="slug"
            ),
        ),
    ]
