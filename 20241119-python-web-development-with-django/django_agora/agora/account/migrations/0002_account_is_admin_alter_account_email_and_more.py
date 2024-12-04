# Generated by Django 5.1.3 on 2024-12-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(
                max_length=255, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]