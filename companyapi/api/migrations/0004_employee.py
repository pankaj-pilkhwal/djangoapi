# Generated by Django 5.0.2 on 2024-02-18 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_delete_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("email", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                ("about", models.TextField(max_length=200)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Manager", "Manager"),
                            ("Software Developer", "Software Developer"),
                            ("Project Leader", "Project Leader"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]