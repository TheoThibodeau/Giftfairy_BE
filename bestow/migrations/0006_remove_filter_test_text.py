# Generated by Django 4.2.4 on 2023-11-01 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0005_filter_test_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='test_text',
        ),
    ]
