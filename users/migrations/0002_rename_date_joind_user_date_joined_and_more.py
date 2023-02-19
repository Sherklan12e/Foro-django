# Generated by Django 4.1.7 on 2023-02-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="date_joind",
            new_name="date_joined",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="is_stuff",
            new_name="is_staff",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
