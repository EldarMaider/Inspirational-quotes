# Generated by Django 4.1.3 on 2022-11-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_delete_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="quote",
            name="description",
            field=models.CharField(max_length=500, null=True),
        ),
    ]