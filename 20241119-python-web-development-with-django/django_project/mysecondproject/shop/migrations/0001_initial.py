# Generated by Django 5.1.3 on 2024-11-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("make", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.DateField()),
                ("description", models.TextField(max_length=500)),
                ("image", models.ImageField(blank=True, upload_to="uploads/")),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]