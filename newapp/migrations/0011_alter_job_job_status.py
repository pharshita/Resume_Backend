# Generated by Django 4.0.5 on 2022-10-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0010_job_job_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_status",
            field=models.CharField(
                choices=[("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")],
                default="ACTIVE",
                max_length=100,
            ),
        ),
    ]
