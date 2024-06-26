# Generated by Django 4.1 on 2024-05-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("email", models.EmailField(max_length=254)),
                ("title", models.TextField(max_length=30)),
                ("description", models.TextField()),
                ("min_pay", models.IntegerField()),
                ("date", models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
