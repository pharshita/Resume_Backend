# Generated by Django 4.0.5 on 2022-10-27 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0005_alter_userinformations_skills"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContectUs",
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
                ("name", models.CharField(blank=True, max_length=25, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="jobapplication",
            name="apply_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
