# Generated by Django 4.2.7 on 2023-11-18 09:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0003_pet_size"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="size",
        ),
    ]