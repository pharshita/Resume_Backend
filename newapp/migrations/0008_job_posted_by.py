# Generated by Django 4.0.5 on 2022-10-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0007_rename_experience_requride_job_experience_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="posted_by",
            field=models.CharField(default="hr", max_length=100),
            preserve_default=False,
        ),
    ]