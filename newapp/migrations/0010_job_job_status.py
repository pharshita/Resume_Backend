# Generated by Django 4.0.5 on 2022-10-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0009_contectus_contact_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="job_status",
            field=models.CharField(
                choices=[("A", "ACTIVE"), ("I", "INACTIVE")],
                default="ACTIVE",
                max_length=100,
            ),
        ),
    ]