# Generated by Django 3.1 on 2020-08-08 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_resource_isdone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='isdone',
        ),
    ]
