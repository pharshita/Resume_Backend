# Generated by Django 3.2 on 2022-08-02 05:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0003_jobapplication_alter_userinformations_skills"),
    ]

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
                ("job_name", models.CharField(blank=True, max_length=105, null=True)),
                ("job_description", models.TextField(blank=True, null=True)),
                ("number_of_openings", models.IntegerField(blank=True, null=True)),
                (
                    "experience_requride",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("responsibilities", models.TextField(blank=True, null=True)),
                (
                    "requirement",
                    models.CharField(
                        choices=[
                            ("python", "Python Developer"),
                            ("react", "React Developer"),
                        ],
                        default="python",
                        max_length=12,
                    ),
                ),
                ("perks_and_benefits", models.TextField(blank=True, null=True)),
                (
                    "skills_required",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
    ]
