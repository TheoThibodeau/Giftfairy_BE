# Generated by Django 4.2.4 on 2023-11-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0009_merge_20231102_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='activity_level',
            field=models.CharField(default='', max_length=300),
        ),
    ]
