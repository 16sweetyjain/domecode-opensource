# Generated by Django 3.1 on 2020-08-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_remove_resource_isdone'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='isdone',
            field=models.BooleanField(default=False),
        ),
    ]