# Generated by Django 4.0.5 on 2022-08-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0002_alter_userinformations_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jobapplication",
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
                ("full_name", models.CharField(blank=True, max_length=120, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                ("resume", models.FileField(upload_to="media")),
            ],
        ),
        migrations.AlterField(
            model_name="userinformations",
            name="skills",
            field=models.ManyToManyField(to="newapp.skillsmodel"),
        ),
    ]
