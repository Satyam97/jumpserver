# Generated by Django 3.2.16 on 2023-04-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0113_auto_20230411_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseautomation',
            name='params',
            field=models.JSONField(default=dict, verbose_name='Params'),
        ),
    ]
