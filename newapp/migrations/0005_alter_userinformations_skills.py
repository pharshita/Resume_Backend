# Generated by Django 3.2 on 2022-08-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformations',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='newapp.SkillsModel'),
        ),
    ]
