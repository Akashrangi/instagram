# Generated by Django 5.0.10 on 2025-01-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("igusers", "0003_likes_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="comment",
            field=models.TextField(default="Enter comment here"),
        ),
    ]
