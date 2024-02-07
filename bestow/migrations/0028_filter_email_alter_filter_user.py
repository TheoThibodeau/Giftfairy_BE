# Generated by Django 4.2.7 on 2024-01-30 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0027_alter_filter_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='email',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='filter',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filters', to=settings.AUTH_USER_MODEL),
        ),
    ]