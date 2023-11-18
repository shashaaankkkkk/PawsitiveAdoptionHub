# Generated by Django 4.2.7 on 2023-11-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("breed", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("photo", models.ImageField(upload_to="pet_photos/")),
                ("medical_history", models.TextField()),
                ("adoption_status", models.BooleanField(default=False)),
            ],
        ),
    ]
