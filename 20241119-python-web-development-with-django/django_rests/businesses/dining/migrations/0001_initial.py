# Generated by Django 5.1.3 on 2024-11-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(max_length=200)),
                ("rating", models.FloatField(null=True)),
                ("review_count", models.IntegerField(null=True)),
                ("price", models.IntegerField(null=True)),
                ("cuisine", models.CharField(blank=True, max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="uploads/")),
                ("address", models.CharField(blank=True, max_length=200)),
                ("city", models.CharField(blank=True, max_length=200)),
                ("zip_code", models.CharField(blank=True, max_length=5)),
                ("state", models.CharField(blank=True, max_length=2)),
                ("phone", models.CharField(max_length=14)),
            ],
        ),
    ]
